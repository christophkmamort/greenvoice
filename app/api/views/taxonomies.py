from url_filter.integrations.drf import DjangoFilterBackend

from rest_framework.filters import OrderingFilter
from rest_framework.viewsets import ModelViewSet

from api.serializers.taxonomies import *
from api.permissions import IsStaffOrReadOnly
from taxonomies.models import *


class CategoryViewSet(ModelViewSet):
    """
    Manage `list`, `create`, `retrieve`, `update` and `destroy` categories.
    """
    queryset = Category.objects.all()
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filter_fields = ['product', 'parent',]
    ordering_fields = ['created', 'value',]
    ordering = ['-value']
    serializer_class = CategorySerializer
    permission_classes = [IsStaffOrReadOnly]


class ColorViewSet(ModelViewSet):
    """
    Manage `list`, `create`, `retrieve`, `update` and `destroy` colors.
    """
    queryset = Color.objects.all()
    filter_backends = [OrderingFilter]
    ordering_fields = ['created', 'value',]
    ordering = ['-value']
    serializer_class = ColorSerializer
    permission_classes = [IsStaffOrReadOnly]


class CountryViewSet(ModelViewSet):
    """
    Manage `list`, `create`, `retrieve`, `update` and `destroy` countries.
    """
    queryset = Country.objects.all()
    filter_backends = [OrderingFilter]
    ordering_fields = ['created', 'value',]
    ordering = ['-value']
    serializer_class = CountrySerializer
    permission_classes = [IsStaffOrReadOnly]


class SizeViewSet(ModelViewSet):
    """
    Manage `list`, `create`, `retrieve`, `update` and `destroy` sizes.
    """
    queryset = Size.objects.all()
    filter_backends = [OrderingFilter]
    ordering_fields = ['order',]
    ordering = ['order']
    serializer_class = SizeSerializer
    permission_classes = [IsStaffOrReadOnly]


class TargetGroupViewSet(ModelViewSet):
    """
    Manage `list`, `create`, `retrieve`, `update` and `destroy` sizes.
    """
    queryset = TargetGroup.objects.all()
    filter_backends = [OrderingFilter]
    ordering_fields = ['value',]
    ordering = ['-value']
    serializer_class = TargetGroupSerializer
    permission_classes = [IsStaffOrReadOnly]
