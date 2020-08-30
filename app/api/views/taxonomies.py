from rest_framework.filters import OrderingFilter
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.viewsets import ModelViewSet

from api.serializers import CategorySerializer, ColorSerializer, SizeSerializer, UserGroupSerializer
from shop.models.taxonomies import Category, Color, Size, UserGroup


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


class SizeViewSet(ModelViewSet):
    """
    Manage `list`, `create`, `retrieve`, `update` and `destroy` sizes.
    """
    queryset = Size.objects.all()
    filter_backends = [OrderingFilter]
    ordering_fields = ['order',]
    ordering = ['order']
    serializer_class = SizeSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class UserGroupViewSet(ModelViewSet):
    """
    Manage `list`, `create`, `retrieve`, `update` and `destroy` sizes.
    """
    queryset = UserGroup.objects.all()
    filter_backends = [OrderingFilter]
    ordering_fields = ['value',]
    ordering = ['-value']
    serializer_class = UserGroupSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
