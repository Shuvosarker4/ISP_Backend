from rest_framework import serializers
from package.models import Package

class PackageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Package
        fields = [
            'id',
            'creator',
            'package_name',
            'package_type',
            'download_speed',
            'upload_speed',
            'data_limit',
            'connection_type',
            'monthly_price',
            'setup_fee',
            'contact_term',
            'package_description',
            'package_status',
            'created_at',
            'updated_at',
        ]
        read_only_fields = ['creator', 'created_at', 'updated_at']
