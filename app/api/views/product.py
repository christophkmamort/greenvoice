from url_filter.integrations.drf import DjangoFilterBackend

from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.viewsets import ModelViewSet

from api.serializers.product import *
from taxonomies.models import Category
from shop.models.product import *


class ProductManagerViewSet(ModelViewSet):
    """
    Manage `list`, `create`, `retrieve`, `update` and `destroy` product manager.
    """
    queryset = ProductManager.objects.all()
    filter_backends = [DjangoFilterBackend, OrderingFilter, SearchFilter]
    filter_fields = ['product__brand']
    ordering_fields = ['created', 'value']
    ordering = ['-created']
    search_fields = ['color__name', 'query'] # Add more search fields
    serializer_class = ProductManagerSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_serializer_class(self):
        """
        Return appropriate serializer class for product manager.
        """
        if self.action == 'retrieve' or self.action == 'list':
            return ProductManagerDetailSerializer
        return self.serializer_class


class ProductOptionViewSet(ModelViewSet):
    """
    Manage `list`, `create`, `retrieve`, `update` and `destroy` product option.
    """
    queryset = ProductOption.objects.all()
    filter_backends = [OrderingFilter] # DjangoFilterBackend
    ordering_fields = ['created', 'gross', 'value']
    ordering = ['-created']
    serializer_class = ProductOptionSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_serializer_class(self):
        """
        Return appropriate serializer class for product option.
        """
        if self.action == 'retrieve' or self.action == 'list':
            return ProductOptionDetailSerializer
        return self.serializer_class


class ProductViewSet(ModelViewSet):
    """
    Manage `list`, `create`, `retrieve`, `update` and `destroy` product.
    """
    queryset = Product.objects.all()
    filter_backends = [OrderingFilter] # DjangoFilterBackend
    filter_fields = ['brand', 'category', 'gender']
    ordering_fields = ['created', 'value']
    ordering = ['-created']
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
