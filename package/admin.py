from django.contrib import admin
from package.models import Package

@admin.register(Package)
class PackageAdmin(admin.ModelAdmin):
    list_display = ('package_name', 'creator', 'monthly_price', 'package_status', 'created_at')
    list_filter = ('package_status', 'contact_term', 'creator')
    search_fields = ('package_name', 'creator__email')
