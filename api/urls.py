from django.urls import path,include
from rest_framework.routers import DefaultRouter
from package.views import PackageViewSet
from customer.views import CustomerViewSet
router = DefaultRouter()
router.register('packages',PackageViewSet,basename='packages')
router.register('customers', CustomerViewSet, basename='customers')

urlpatterns = [
    path('',include(router.urls)),
]