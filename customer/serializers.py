from rest_framework import serializers
from customer.models import Customer

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = [
            'id',
            'reseller',
            'first_name',
            'last_name',
            'email',
            'phone_number',
            'alternative_phone_number',
            'prefer_contact_method',
            'address',
            'city',
            'package',
            'connection_type',
            'connection_date',
            'note',
            'account_status',
            'is_billed',
            'created_at',
            'updated_at',
        ]
        read_only_fields = ['reseller','created_at', 'updated_at']
