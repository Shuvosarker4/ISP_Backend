from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from .models import Package
from .serializers import PackageSerializer

class PackageViewSet(ModelViewSet):
    serializer_class = PackageSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Package.objects.filter(creator=self.request.user)

    def perform_create(self, serializer):
        serializer.save(creator=self.request.user)
