from url_filter.integrations.drf import DjangoFilterBackend

from rest_framework.filters import OrderingFilter
from rest_framework.permissions import IsAdminUser
from rest_framework.viewsets import ModelViewSet

from api.serializers.taxonomies import *
from api.permissions import ReadOnly
from taxonomies.models import *


class CategoryViewSet(ModelViewSet):
    """
    Manage `list`, `create`, `retrieve`, `update` and `destroy`.
    """
    queryset = Category.objects.all()
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filter_fields = ['product', 'parent',]
    ordering_fields = ['created', 'value',]
    ordering = ['-value']
    serializer_class = CategorySerializer
    permission_classes = [IsAdminUser|ReadOnly]

    def get_serializer_class(self):
        """
        Return appropriate serializer class for product manager.
        """
        if self.action == 'retrieve' or self.action == 'list':
            return CategoryDetailMiniSerializer
        return self.serializer_class


class ColorViewSet(ModelViewSet):
    """
    Manage `list`, `create`, `retrieve`, `update` and `destroy`.
    """
    queryset = Color.objects.all()
    filter_backends = [OrderingFilter]
    ordering_fields = ['created', 'value',]
    ordering = ['-value']
    serializer_class = ColorSerializer
    permission_classes = [IsAdminUser|ReadOnly]


class SizeViewSet(ModelViewSet):
    """
    Manage `list`, `create`, `retrieve`, `update` and `destroy`.
    """
    queryset = Size.objects.all()
    filter_backends = [OrderingFilter]
    ordering_fields = ['order',]
    ordering = ['order']
    serializer_class = SizeSerializer
    permission_classes = [IsAdminUser|ReadOnly]


class TargetGroupViewSet(ModelViewSet):
    """
    Manage `list`, `create`, `retrieve`, `update` and `destroy`.
    """
    queryset = TargetGroup.objects.all()
    filter_backends = [OrderingFilter]
    ordering_fields = ['value',]
    ordering = ['-value']
    serializer_class = TargetGroupSerializer
    permission_classes = [IsAdminUser|ReadOnly]
