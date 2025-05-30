from rest_framework import serializers
from payment.models import Payment
from customer.models import Customer

class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = [
            'id',
            'customer',
            'amount',
            'payment_method',
            'payment_date',
            'payment_reference',
            'status',
            'created_at',
            'updated_at',
        ]
        read_only_fields = ['created_at', 'updated_at']

    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     request = self.context.get('request', None)
    #     if request:
    #         self.fields['customer'].queryset = Customer.objects.filter(reseller=request.user)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        request = self.context.get('request', None)
        if request and hasattr(request, 'user') and request.user.is_authenticated:
            self.fields['customer'].queryset = Customer.objects.filter(reseller=request.user)
        else:
            self.fields['customer'].queryset = Customer.objects.none()