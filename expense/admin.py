

from django.contrib import admin
from expense.models import Expense, Category

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'reseller', 'created_at')
    list_filter = ('reseller',)
    search_fields = ('name',)

@admin.register(Expense)
class ExpenseAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'reseller', 'amount', 'priority', 'status', 'date')
    list_filter = ('reseller', 'priority', 'status')
    search_fields = ('title', 'description')
