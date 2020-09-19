from rest_framework.filters import OrderingFilter
from rest_framework.viewsets import ModelViewSet

from api.serializers.product_option import ProductOptionSerializer
from api.permissions import IsStaffOrReadOnly
from shop.models.product import ProductOption


class ProductOptionViewSet(ModelViewSet):
    """
    Manage `list`, `create`, `retrieve`, `update` and `destroy` product option.
    """
    queryset = ProductOption.objects.all()
    filter_backends = [OrderingFilter]
    ordering_fields = ['created', 'gross', 'value']
    ordering = ['-created']
    serializer_class = ProductOptionSerializer
    permission_classes = [IsStaffOrReadOnly]
