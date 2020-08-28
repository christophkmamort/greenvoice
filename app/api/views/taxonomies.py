from rest_framework.filters import OrderingFilter
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.viewsets import ModelViewSet

from api.serializers import CategorySerializer, ColorSerializer, SizeSerializer
from shop.models.taxonomies import Category, Color, Size


class CategoryViewSet(ModelViewSet):
    """
    Manage `list`, `create`, `retrieve`, `update` and `destroy` categories.
    """
    queryset = Category.objects.all()
    filter_backends = [OrderingFilter]
    ordering_fields = ['created', 'value',]
    ordering = ['-value']
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(slug=self.request.data['name'].lower())


class ColorViewSet(ModelViewSet):
    """
    Manage `list`, `create`, `retrieve`, `update` and `destroy` colors.
    """
    queryset = Color.objects.all()
    filter_backends = [OrderingFilter]
    ordering_fields = ['created', 'value',]
    ordering = ['-value']
    serializer_class = ColorSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(slug=self.request.data['name'].lower())


class SizeViewSet(ModelViewSet):
    """
    Manage `list`, `create`, `retrieve`, `update` and `destroy` sizes.
    """
    queryset = Size.objects.all()
    filter_backends = [OrderingFilter]
    ordering_fields = ['created', 'value',]
    serializer_class = SizeSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(slug=self.request.data['name'].lower())
