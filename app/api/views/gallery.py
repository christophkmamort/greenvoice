from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from api.serializers.gallery import ProductBrandGallerySerializer, ProductGallerySerializer
from shop.models.gallery import ProductBrandImage, ProductImage


class ProductBrandGalleryViewSet(ModelViewSet):
    """
    Manage `list`, `create`, `retrieve`, `update` and `destroy` product brand img.
    """
    queryset = ProductBrandImage.objects.all()
    serializer_class = ProductBrandGallerySerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save()


class ProductGalleryViewSet(ModelViewSet):
    """
    Manage `list`, `create`, `retrieve`, `update` and `destroy` product img.
    """
    queryset = ProductImage.objects.all()
    serializer_class = ProductGallerySerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save()
