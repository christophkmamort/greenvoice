from url_filter.integrations.drf import DjangoFilterBackend

from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.viewsets import ModelViewSet

from api.serializers.product import ProductManagerSerializer, \
                                    ProductManagerDetailSerializer, \
                                    ProductOptionSerializer, ProductSerializer
from taxonomies.models import Category
from shop.models.product import Product, ProductManager, ProductOption


class ProductManagerViewSet(ModelViewSet):
    """
    Manage `list`, `create`, `retrieve`, `update` and `destroy` product manager.
    """
    queryset = ProductManager.objects.all()
    filter_backends = [DjangoFilterBackend, OrderingFilter, SearchFilter]
    filter_fields = ['product__brand']
    ordering_fields = ['created', 'value']
    ordering = ['-created']
    search_fields = ['color__name'] # Add more search fields
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

    # Create logic to fill gross, tax and net if nessasary!! & make sure that it is filled correct!!


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

    """def perform_create(self, serializer):
        categories = self.request.data.getlist('category')
        query = ''
        for id in categories:
            category = Category.objects.get(id=id)
            query += category.name + ' '
        gender = self.request.data.get('gender')
        if gender == '1':
            query += 'Unisex Frauen Damen Herren Männer '
        if gender == '2':
            query += 'Frauen Damen '
        if gender == '3':
            query += 'Herren Männer '
        serializer.save(query=query)

    def perform_update(self, serializer):
        categories = self.request.data.getlist('category')
        query = ''
        for id in categories:
            category = Category.objects.get(id=id)
            query += category.name + ' '
        gender = self.request.data.get('gender')
        if gender == '1':
            query += 'Unisex Frauen Damen Herren Männer '
        if gender == '2':
            query += 'Frauen Damen '
        if gender == '3':
            query += 'Herren Männer '
        serializer.save(query=query)"""
