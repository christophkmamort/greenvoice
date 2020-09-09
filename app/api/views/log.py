from rest_framework.filters import OrderingFilter
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from api.serializers.log import BrandValueLogSerializer, ProductValueLogSerializer, TaxonomyValueLogSerializer
from logs.models import BrandValueLog, ProductValueLog, TaxonomyValueLog


class BaseValueLog(ModelViewSet):
    filter_backends = [OrderingFilter]
    ordering_fields = ['created',]
    ordering = ['-created']

    def perform_create(self, serializer):
        serializer.save()


class BrandValueLogViewSet(BaseValueLog):
    """
    Manage `list`, `create`, `retrieve`, `update` and `destroy` product log.
    """
    queryset = BrandValueLog.objects.all()
    serializer_class = BrandValueLogSerializer


class ProductValueLogViewSet(BaseValueLog):
    """
    Manage `list`, `create`, `retrieve`, `update` and `destroy` product log.
    """
    queryset = ProductValueLog.objects.all()
    serializer_class = ProductValueLogSerializer


class TaxonomyValueLogViewSet(BaseValueLog):
    """
    Manage `list`, `create`, `retrieve`, `update` and `destroy` product log.
    """
    queryset = TaxonomyValueLog.objects.all()
    serializer_class = TaxonomyValueLogSerializer
