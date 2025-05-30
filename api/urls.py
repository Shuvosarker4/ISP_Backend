from django.urls import path,include
from rest_framework.routers import DefaultRouter
from package.views import PackageViewSet
from customer.views import CustomerViewSet
from payment.views import PaymentViewSet
from expense.views import ExpenseViewSet,CategoryViewSet


router = DefaultRouter()
router.register('packages',PackageViewSet,basename='packages')
router.register('customers', CustomerViewSet, basename='customers')
router.register('payments', PaymentViewSet,basename='payments')
router.register('categories', CategoryViewSet, basename='categories')
router.register('expenses', ExpenseViewSet, basename='expenses')

urlpatterns = [
    path('',include(router.urls)),
    path('dashboard/', include('dashboard.urls')),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')), 
]