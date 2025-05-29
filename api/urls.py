from django.urls import path,include
from rest_framework.routers import DefaultRouter
from package.views import PackageViewSet
router = DefaultRouter()
router.register('packages',PackageViewSet,basename='packages')

urlpatterns = [
    path('',include(router.urls)),
]