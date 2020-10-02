from rest_framework.viewsets import ModelViewSet

from api.serializers.helper import *
from api.permissions import IsUserOrStaff
from shop.models.api import BasicApi
from shop.models.banking import BasicBanking
from shop.models.brand import BasicBranding
from shop.models.imprint import BasicImprint
from shop.models.meta_data import BasicMetaData
from shop.models.settings import BrandSettings
from shop.models.tax import BasicTax


"""
Universal.
"""
# class BasicMetaDataViewSet(ModelViewSet):
"""
Manage `list`, `create`, `retrieve`, `update` and `destroy`.
"""
""" queryset = BasicMetaData.objects.all()
serializer_class = BasicMetaDataSerializer
permission_classes = [IsUserOrStaff] """


"""
Brand.
"""
class BankingViewSet(ModelViewSet):
    """
    Manage `list`, `create`, `retrieve`, `update` and `destroy`.
    """
    queryset = BasicBanking.objects.all()
    serializer_class = BasicBankingSerializer
    permission_classes = [IsUserOrStaff]
