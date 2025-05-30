from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from customer.models import Customer
from customer.serializers import CustomerSerializer
from rest_framework.permissions import IsAuthenticated

class CustomerViewSet(ModelViewSet):
    serializer_class = CustomerSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        if user.is_authenticated:
            return Customer.objects.filter(reseller=user).order_by('-created_at')
        return Customer.objects.none()

    def perform_create(self, serializer):
        serializer.save(reseller=self.request.user)
