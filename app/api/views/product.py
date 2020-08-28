from url_filter.integrations.drf import DjangoFilterBackend

from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.viewsets import ModelViewSet

from api.serializers.product import ProductOptionSerializer, ProductSerializer
from shop.models.taxonomies import Category
from shop.models.product import Product, ProductOption


class ProductOptionViewSet(ModelViewSet):
    queryset = ProductOption.objects.all()
    filter_backends = [DjangoFilterBackend, OrderingFilter, SearchFilter]
    ordering_fields = ['created', 'gross', 'value']
    ordering = ['-value']
    serializer_class = ProductOptionSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save()


class ProductViewSet(ModelViewSet):
    """
    Manage `list`, `create`, `retrieve`, `update` and `destroy` products.
    """
    queryset = Product.objects.all()
    filter_backends = [DjangoFilterBackend, OrderingFilter, SearchFilter]
    filter_fields = ['brand', 'category', 'gender'] # , 'price'
    ordering_fields = ['created', 'value'] #  'price',
    ordering = ['-value']
    search_fields = ['brand__name', 'name', 'query']
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
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
        print(query)
        serializer.save(query=query)
