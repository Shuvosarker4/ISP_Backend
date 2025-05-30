from djoser.serializers import UserCreateSerializer as BaseUserCreateSerializer, UserSerializer as BaseUserSerializer

class UserCreateSerializer(BaseUserCreateSerializer):
    class Meta(BaseUserCreateSerializer.Meta):
        fields = [
            'id',
            'company_name',
            'business_type',
            'registration_number',
            'tax_id',
            'contact_person',
            'position_type',
            'email',
            'password',
            'phone_number',
            'alternative_phone',
            'website',
            'address',
            'services',
            'notes',
            'account_type',
            'created_at',
            'updated_at',
        ]
        read_only_fields = ['account_type']


class UserSerializer(BaseUserSerializer):
    class Meta(BaseUserSerializer.Meta):
        ref_name = 'CustomUser'
        fields = [
            'id',
            'company_name',
            'business_type',
            'registration_number',
            'tax_id',
            'contact_person',
            'position_type',
            'email',
            'phone_number',
            'alternative_phone',
            'website',
            'address',
            'services',
            'notes',
            'account_type',
            'created_at',
            'updated_at',
        ]
        read_only_fields = ['account_type']
