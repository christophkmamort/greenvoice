from rest_framework.filters import OrderingFilter
from rest_framework.viewsets import ModelViewSet

from api.serializers.log import *
from logs.models import *


class BaseValueLog(ModelViewSet):
    filter_backends = [OrderingFilter]
    ordering_fields = ['created',]
    ordering = ['-created']


class BrandValueLogViewSet(BaseValueLog):
    """
    Manage `list`, `create`, `retrieve`, `update` and `destroy`.
    """
    queryset = BrandValueLog.objects.all()
    serializer_class = BrandValueLogSerializer


class ProductValueLogViewSet(BaseValueLog):
    """
    Manage `list`, `create`, `retrieve`, `update` and `destroy`.
    """
    queryset = ProductValueLog.objects.all()
    serializer_class = ProductValueLogSerializer


class TaxonomyValueLogViewSet(BaseValueLog):
    """
    Manage `list`, `create`, `retrieve`, `update` and `destroy`.
    """
    queryset = TaxonomyValueLog.objects.all()
    serializer_class = TaxonomyValueLogSerializer
