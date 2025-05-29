# payment/admin.py

from django.contrib import admin
from .models import Payment

@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = (
        'payment_reference',
        'customer',
        'amount',
        'payment_method',
        'status',
        'payment_date',
        'created_at',
    )
    list_filter = (
        'payment_method',
        'status',
        'payment_date',
        'created_at',
    )
    search_fields = (
        'payment_reference',
        'customer__first_name',
        'customer__last_name',
        'customer__email',
    )
    ordering = ('-created_at',)
