from django.db import models
from users.models import User

class Package(models.Model):
    CONTACT_TERM_CHOICES = [
    ('no', 'No Term'),
    ('monthly', 'Monthly'),
    ('quarterly', 'Quarterly'),
    ('yearly', 'Yearly'),
    ]

    PACKAGE_TYPES = [
        ('business', 'Business'),
        ('student', 'Student'),
        ('premium', 'Premium'),
        ('basic', 'Basic'),
        ]

    STATUS_CHOICES = [
    ('active', 'Active'),
    ('inactive', 'Inactive'),
    ('upcoming', 'Upcoming'),
    ]

    DATALIMIT_CHOICES = [
        ('unlimited', 'Unlimited'),
        ('100gb', '100 GB'),
        ('500gb', '500 GB'),
        ('1tb', '1 TB'),
        ('2tb', '2 TB'),
        ]
    
    CONNECTION_CHOICES = [
        ('Fiber', 'Fiber'),
        ('DSL', 'DSL'),
        ('Broadband', 'Broadband'),
    ]

    creator = models.ForeignKey(User, on_delete=models.CASCADE, related_name='packages')
    package_name = models.CharField(max_length=100)
    package_type = models.CharField(max_length=100,choices=PACKAGE_TYPES)
    download_speed = models.CharField(max_length=50)
    upload_speed = models.CharField(max_length=50)
    data_limit = models.CharField(max_length=50,choices=DATALIMIT_CHOICES)
    connection_type = models.CharField(max_length=50,choices=CONNECTION_CHOICES)
    monthly_price = models.DecimalField(max_digits=8, decimal_places=2)
    setup_fee = models.DecimalField(max_digits=8,decimal_places=2)
    contact_term = models.CharField(max_length=20,choices=CONTACT_TERM_CHOICES)
    package_description= models.TextField()
    package_status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='active')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.package_name} - {self.download_speed}/{self.upload_speed} - {self.monthly_price}"

