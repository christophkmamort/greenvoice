from rest_framework.viewsets import ModelViewSet

from api.serializers.media import ProductBrandImageSerializer, ProductImageSerializer
from api.permissions import IsStaffOrReadOnly
from shop.models.media import ProductBrandImage, ProductImage


class ProductBrandImageViewSet(ModelViewSet):
    """
    Manage `list`, `create`, `retrieve`, `update` and `destroy`.
    """
    queryset = ProductBrandImage.objects.all()
    serializer_class = ProductBrandImageSerializer
    permission_classes = [IsStaffOrReadOnly]

    def perform_create(self, serializer):
        serializer.save()


class ProductImageViewSet(ModelViewSet):
    """
    Manage `list`, `create`, `retrieve`, `update` and `destroy`.
    """
    queryset = ProductImage.objects.all()
    serializer_class = ProductImageSerializer
    permission_classes = [IsStaffOrReadOnly]

    def perform_create(self, serializer):
        serializer.save()
