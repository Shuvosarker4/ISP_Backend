from django.db import models
from users.models import User
from package.models import Package

# Create your models here.
class Customer(models.Model):

    CONNECTION_CHOICES = [
        ('Fiber', 'Fiber'),
        ('DSL', 'DSL'),
        ('Broadband', 'Broadband'),
    ]

    CONTACT_METHOD_CHOICES = [
        ('Phone', 'Phone'),
        ('Email', 'Email'),
        ('WhatsApp', 'WhatsApp'),
    ]

    ACCOUNT_STATUS_CHOICES = [
        ('Active', 'Active'),
        ('Pending', 'Pending'),
        ('Suspended', 'Suspended'),
    ]

    reseller = models.ForeignKey(User, on_delete=models.CASCADE, related_name='customers')
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True, null=True, blank=True, db_index=True)
    phone_number = models.CharField(max_length=20, null=True, blank=True)
    alternative_phone_number = models.CharField(max_length=20, null=True, blank=True)
    prefer_contact_method = models.CharField(max_length=20,choices=CONTACT_METHOD_CHOICES)
    address = models.TextField(null=True, blank=True)
    city = models.TextField(null=True, blank=True)
    package = models.ForeignKey(Package,on_delete=models.SET_NULL, null=True, blank=True)
    connection_type = models.CharField(max_length=20,choices=CONNECTION_CHOICES)
    connection_date = models.DateTimeField(auto_now_add=True)
    note = models.TextField(null=True, blank=True)
    account_status = models.CharField(max_length=20,choices=ACCOUNT_STATUS_CHOICES)
    is_billed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.connection_type} - {self.package}"
