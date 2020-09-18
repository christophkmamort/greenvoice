from url_filter.integrations.drf import DjangoFilterBackend

from rest_framework.filters import OrderingFilter
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.viewsets import ModelViewSet

from api.serializers.brand import BrandDetailSerializer, BrandSerializer
from shop.models.brand import Brand


class BrandViewSet(ModelViewSet):
    """
    Manage `list`, `create`, `retrieve`, `update` and `destroy`.
    """
    queryset = Brand.objects.all()
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filter_fields = ['status', 'product']
    ordering_fields = ['created', 'value',]
    ordering = ['-created']
    serializer_class = BrandSerializer
    permission_classes = [IsAuthenticatedOrReadOnly] # Add is staff to edit.

    def get_serializer_class(self):
        """
        Return appropriate serializer class.
        """
        if self.action == 'retrieve' or self.action == 'list':
            return BrandDetailSerializer
        return self.serializer_class
