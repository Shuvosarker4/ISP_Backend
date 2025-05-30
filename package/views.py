from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from package.models import Package
from package.serializers import PackageSerializer

class PackageViewSet(ModelViewSet):
    serializer_class = PackageSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        if user.is_authenticated:
            return Package.objects.filter(creator=user)
        return Package.objects.none()


    def perform_create(self, serializer):
        serializer.save(creator=self.request.user)
