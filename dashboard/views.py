from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from customer.models import Customer
from payment.models import Payment
from expense.models import Expense, Category
from package.models import Package
from django.utils import timezone
from django.db.models import Sum, Q, Count, F, ExpressionWrapper, DecimalField
from datetime import timedelta

class DashboardSummaryView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        today = timezone.now().date()
        start_of_week = today - timedelta(days=today.weekday())
        start_of_month = today.replace(day=1)

        # Total customers
        total_customers = Customer.objects.filter(reseller=user).count()

        # Total collection
        total_collection = Payment.objects.filter(
            customer__reseller=user,
            status='complete'
        ).aggregate(total=Sum('amount'))['total'] or 0

        # Today's collection
        today_collection = Payment.objects.filter(
            customer__reseller=user,
            status='complete',
            payment_date=today
        ).aggregate(total=Sum('amount'))['total'] or 0

        # Weekly collection
        weekly_collection = Payment.objects.filter(
            customer__reseller=user,
            status='complete',
            payment_date__gte=start_of_week
        ).aggregate(total=Sum('amount'))['total'] or 0

        # Monthly collection
        monthly_collection = Payment.objects.filter(
            customer__reseller=user,
            status='complete',
            payment_date__gte=start_of_month
        ).aggregate(total=Sum('amount'))['total'] or 0

        # Pending dues
        pending_due = Payment.objects.filter(
            customer__reseller=user,
            status='pending'
        ).aggregate(total=Sum('amount'))['total'] or 0

        active_packages = Package.objects.filter(
            package_status='active',
            creator=user
        ).annotate(
            customer_count=Count('customer', filter=Q(customer__reseller=user))
        ).annotate(
            revenue=ExpressionWrapper(F('customer_count') * F('monthly_price'), output_field=DecimalField()),
            setup_fee_collection=ExpressionWrapper(F('customer_count') * F('setup_fee'), output_field=DecimalField())
        )

        active_packages_count = active_packages.count()  # <-- Added this line

        totals = active_packages.aggregate(
            total_revenue=Sum('revenue'),
            total_setup_fee=Sum('setup_fee_collection')
        )

        active_package_revenue = totals['total_revenue'] or 0
        total_setup_fee_collection = totals['total_setup_fee'] or 0

        return Response({
            'total_customers': total_customers,
            'total_collection': total_collection,
            'today_collection': today_collection,
            'weekly_collection': weekly_collection,
            'monthly_collection': monthly_collection,
            'pending_due': pending_due,
            'active_package_revenue': active_package_revenue,
            'active_packages': active_packages_count,
            'total_setup_fee_collection': total_setup_fee_collection,
        })


class ExpenseSummaryView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        today = timezone.now().date()
        first_day_this_month = today.replace(day=1)
        last_month_end = first_day_this_month - timedelta(days=1)
        last_month_start = last_month_end.replace(day=1)

        # Total expense for reseller
        total_expense = Expense.objects.filter(reseller=user).aggregate(total=Sum('amount'))['total'] or 0

        # Expense grouped by category for reseller
        categories = Category.objects.filter(reseller=user)
        category_expenses = (
            Expense.objects
            .filter(reseller=user, category__in=categories)
            .values('category__name')
            .annotate(total=Sum('amount'))
            .order_by('-total')
        )

        # Last month expense total
        last_month_expense = Expense.objects.filter(
            reseller=user,
            date__gte=last_month_start,
            date__lte=last_month_end,
        ).aggregate(total=Sum('amount'))['total'] or 0

        return Response({
            'total_expense': total_expense,
            'category_expenses': category_expenses,
            'last_month_expense': last_month_expense,
        })
