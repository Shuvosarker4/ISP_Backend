
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from .models import Expense, Category
from .serializers import ExpenseSerializer, CategorySerializer

class CategoryViewSet(ModelViewSet):
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        if user.is_authenticated:
            return Category.objects.filter(reseller=user).order_by('-created_at')
        else:
            return Category.objects.none()

    def perform_create(self, serializer):
        serializer.save(reseller=self.request.user)

class ExpenseViewSet(ModelViewSet):
    serializer_class = ExpenseSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        if user.is_authenticated:
            return Expense.objects.filter(reseller=user).order_by('-created_at')
        else:
            # Return empty queryset if user is anonymous (e.g. during swagger schema generation)
            return Expense.objects.none()
        

    def perform_create(self, serializer):
        serializer.save(reseller=self.request.user)
