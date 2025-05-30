from rest_framework import serializers
from expense.models import Expense, Category

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = [
            'id',
            'name',
            'reseller',
            'created_at',
            'updated_at',
        ]
        read_only_fields = ['reseller', 'created_at', 'updated_at']

class ExpenseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Expense
        fields = [
            'id',
            'reseller',
            'category',
            'date',
            'amount',
            'priority',
            'title',
            'description',
            'payment',
            'status',
            'created_at',
            'updated_at',
        ]
        read_only_fields = ['reseller', 'created_at', 'updated_at']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        request = self.context.get('request', None)
        if request and hasattr(request, 'user') and request.user.is_authenticated:
            self.fields['category'].queryset = Category.objects.filter(reseller=request.user)
        else:
            self.fields['category'].queryset = Category.objects.none()