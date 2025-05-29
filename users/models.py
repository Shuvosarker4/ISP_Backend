from django.db import models
from django.contrib.auth.models import AbstractUser
from users.managers import CustomUserManager
from multiselectfield import MultiSelectField

# Create your models here.

class User(AbstractUser):
    BUSINESS_TYPE_CHOICES = [
    ('isp', 'Internet Service Provider (ISP)'),
    ('regional_partner', 'Regional Partner'),
    ('local_distributor', 'Local Distributor'),
    ('premium_reseller', 'Premium Reseller'),
    ]

    BUSINESS_POSITION_CHOICES = [
    ('owner', 'Owner'),
    ('manager', 'Manager'),
    ('sales_manager', 'Sales Manager'),
    ('technician', 'Technician'),
    ('accountant', 'Accountant'),
    ('customer_support', 'Customer Support'),
    ('marketing_exec', 'Marketing Executive'),
    ]
    SERVICES_CHOICES = [
    ('sales', 'Sales Support'),
    ('customer', 'Customer Service'),
    ('technical', 'Technical Support'),
    ('billing', 'Billing Management'),
    ('installation', 'Installation Services'),
    ('marketing', 'Marketing Support'),
    ('maintenance', 'Maintenance Services'),
    ('training', 'Training Programs'),
    ]
    

    username = None
    company_name = models.CharField(max_length=15)
    business_type = models.CharField(choices=BUSINESS_TYPE_CHOICES)
    registration_number = models.CharField(max_length=15)
    tax_id = models.CharField(max_length=15)
    contact_person = models.CharField(max_length=15)
    position_type = models.CharField(choices=BUSINESS_POSITION_CHOICES)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15,blank=True,null=True)
    alternative_phone = models.CharField(max_length=15,blank=True,null=True)
    website = models.URLField(blank=True, null=True)
    address = models.TextField(max_length=20,blank=True,null=True)
    services = MultiSelectField(choices=SERVICES_CHOICES, max_length=200)
    notes = models.TextField()
    is_active = models.BooleanField(default=True)
    account_type=models.CharField(default="Reseller")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS=[]

    objects = CustomUserManager()

    def __str__(self):
        return self.email
