
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from .models import Expense, Category
from .serializers import ExpenseSerializer, CategorySerializer

class CategoryViewSet(ModelViewSet):
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Category.objects.filter(reseller=self.request.user).order_by('-created_at')

    def perform_create(self, serializer):
        serializer.save(reseller=self.request.user)

class ExpenseViewSet(ModelViewSet):
    serializer_class = ExpenseSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Expense.objects.filter(reseller=self.request.user).order_by('-created_at')

    def perform_create(self, serializer):
        serializer.save(reseller=self.request.user)
