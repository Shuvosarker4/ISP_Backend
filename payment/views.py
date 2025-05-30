from rest_framework.viewsets import ModelViewSet
from payment.models import Payment
from payment.serializers import PaymentSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.permissions import IsAuthenticated
from payment.models import Payment
from payment.serializers import PaymentSerializer


class PaymentViewSet(ModelViewSet):
    serializer_class = PaymentSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        if user.is_authenticated:
            return Payment.objects.filter(customer__reseller=user).order_by('-created_at')
        else:
            return Payment.objects.none()

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context.update({"request": self.request})
        return context


# class PaymentViewSet(ModelViewSet):
#     serializer_class = PaymentSerializer
#     permission_classes = [IsAuthenticated]

#     def get_queryset(self):
#         return Payment.objects.filter(customer__reseller=self.request.user).order_by('-created_at')

#     def get_serializer(self, *args, **kwargs):
#         serializer = super().get_serializer(*args, **kwargs)
#         if not isinstance(serializer, serializers.ListSerializer):
#             serializer.fields['customer'].queryset = Customer.objects.filter(reseller=self.request.user)
#         return serializer
