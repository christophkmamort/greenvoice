from rest_framework.serializers import ModelSerializer

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
class BasicMetaDataSerializer(ModelSerializer):
    class Meta:
        model = BasicMetaData
        fields = '__all__'


"""
Brand.
"""
class BasicApiSerializer(ModelSerializer):
    class Meta:
        model = BasicApi
        fields = '__all__'


class BasicBrandingSerializer(ModelSerializer):
    class Meta:
        model = BasicBranding
        fields = '__all__'


class BasicBankingSerializer(ModelSerializer):
    class Meta:
        model = BasicBanking
        fields = '__all__'


class BasicImprintSerializer(ModelSerializer):
    class Meta:
        model = BasicImprint
        fields = '__all__'


class BrandSettingsSerializer(ModelSerializer):
    class Meta:
        model = BrandSettings
        fields = '__all__'


class BasicTaxSerializer(ModelSerializer):
    class Meta:
        model = BasicTax
        fields = '__all__'
