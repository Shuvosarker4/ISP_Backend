from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from users.models import User

class CustomUserAdmin(UserAdmin):
    model = User
    list_display = (
        'email', 'company_name', 'account_type', 
        'position_type', 'is_active', 'is_staff'
    )
    list_filter = ('is_staff', 'is_active', 'account_type', 'position_type')

    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Company Info', {'fields': (
            'company_name', 'business_type', 'registration_number', 'tax_id',
            'contact_person', 'position_type', 'account_type', 'services',
            'website', 'address', 'notes'
        )}),
        ('Personal Info', {'fields': ('first_name', 'last_name', 'phone_number', 'alternative_phone')}),
        ('Permissions', {'fields': (
            'is_staff', 'is_active', 'is_superuser', 'groups', 'user_permissions'
        )}),
        ('Important Dates', {'fields': ('last_login', 'date_joined')})
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': (
                'email', 'password1', 'password2', 
                'company_name', 'account_type', 'position_type', 
                'is_staff', 'is_active'
            ),
        }),
    )

    search_fields = ('email', 'company_name', 'contact_person')
    ordering = ('email',)

admin.site.register(User, CustomUserAdmin)
