from url_filter.integrations.drf import DjangoFilterBackend

from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.viewsets import ModelViewSet

from api.serializers.product_manager import ProductManagerSerializer, ProductManagerDetailSerializer
from shop.models.product import ProductManager


class ProductManagerViewSet(ModelViewSet):
    """
    Manage `list`, `create`, `retrieve`, `update` and `destroy` product manager.
    """
    queryset = ProductManager.objects.all()
    filter_backends = [DjangoFilterBackend, OrderingFilter, SearchFilter]
    filter_fields = ['product', 'product_option']
    ordering_fields = ['created', 'value']
    ordering = ['-created']
    search_fields = ['color__name', 'query']
    serializer_class = ProductManagerSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_serializer_class(self):
        """
        Return appropriate serializer class for product manager.
        """
        if self.action == 'retrieve' or self.action == 'list':
            return ProductManagerDetailSerializer
        return self.serializer_class
