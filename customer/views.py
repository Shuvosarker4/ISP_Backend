from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from customer.models import Customer
from customer.serializers import CustomerSerializer
from rest_framework.permissions import IsAuthenticated

class CustomerViewSet(ModelViewSet):
    serializer_class = CustomerSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Customer.objects.filter(reseller=self.request.user).order_by('-created_at')

    def perform_create(self, serializer):
        serializer.save(reseller=self.request.user)
