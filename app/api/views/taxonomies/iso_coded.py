from rest_framework.filters import OrderingFilter
from rest_framework.permissions import IsAdminUser
from rest_framework.viewsets import ModelViewSet

from api.serializers.taxonomies.iso_coded import *
from api.permissions import ReadOnly
from taxonomies.models.iso_coded import *


class CountryViewSet(ModelViewSet):
    """
    Manage `list`, `create`, `retrieve`, `update` and `destroy`.
    """
    queryset = Country.objects.all()
    filter_backends = [OrderingFilter]
    ordering_fields = ['name',]
    ordering = ['name']
    serializer_class = CountrySerializer
    permission_classes = [IsAdminUser|ReadOnly]


class CompanyTypeViewSet(ModelViewSet):
    """
    Manage `list`, `create`, `retrieve`, `update` and `destroy`.
    """
    queryset = CompanyType.objects.all()
    filter_backends = [OrderingFilter]
    ordering_fields = ['name',]
    ordering = ['name']
    serializer_class = CompanyTypeSerializer
    permission_classes = [IsAdminUser|ReadOnly]


class CurrencyViewSet(ModelViewSet):
    """
    Manage `list`, `create`, `retrieve`, `update` and `destroy`.
    """
    queryset = Currency.objects.all()
    filter_backends = [OrderingFilter]
    ordering_fields = ['name',]
    ordering = ['name']
    serializer_class = CurrencySerializer
    permission_classes = [IsAdminUser|ReadOnly]
