from rest_framework.filters import OrderingFilter
from rest_framework.viewsets import ModelViewSet

from api.serializers.product import ProductSerializer
from api.permissions import IsStaffOrReadOnly
from shop.models.product import Product


class ProductViewSet(ModelViewSet):
    """
    Manage `list`, `create`, `retrieve`, `update` and `destroy` product.
    """
    queryset = Product.objects.all()
    filter_backends = [OrderingFilter]
    ordering_fields = ['created', 'value']
    ordering = ['-created']
    serializer_class = ProductSerializer
    permission_classes = [IsStaffOrReadOnly]
