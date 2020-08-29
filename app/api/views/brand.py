from url_filter.integrations.drf import DjangoFilterBackend

from rest_framework.filters import OrderingFilter
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.viewsets import ModelViewSet

from api.serializers.brand import BrandSerializer
from shop.models.brand import Brand


class BrandViewSet(ModelViewSet):
    """
    Manage `list`, `create`, `retrieve`, `update` and `destroy` brands.
    """
    queryset = Brand.objects.all()
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filter_fields = ['status', 'product']
    ordering_fields = ['created', 'value',]
    ordering = ['-value']
    serializer_class = BrandSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        name = self.request.data.get('name')
        serializer.save()
