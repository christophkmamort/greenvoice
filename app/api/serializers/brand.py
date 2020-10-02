from rest_framework.serializers import ModelSerializer

from .helper import BasicApiSerializer, BasicBrandingSerializer, \
                    BasicBankingSerializer, BasicImprintSerializer, \
                    BrandSettingsSerializer, BasicTaxSerializer # , \ BasicMetaDataSerializer
from .product_option import ProductOptionStatusSerializer
from .taxonomies import CategoryMiniSerializer
from shop.models.brand import Brand
from shop.models.product import Product, ProductManager, ProductOption


"""
Basic serializers.
"""
class BrandSerializer(ModelSerializer):
    api = BasicApiSerializer()
    branding = BasicBrandingSerializer()
    banking = BasicBankingSerializer()
    imprint = BasicImprintSerializer()
    # meta_data = BasicMetaDataSerializer()
    settings = BrandSettingsSerializer()
    tax = BasicTaxSerializer()

    class Meta:
        model = Brand
        fields = '__all__'


"""
Detail serializers to check if brand is active
and has active products in stock.
"""
"""class ProductManagerProductOptionSerializer(ModelSerializer):
    product_option = ProductOptionStatusSerializer(read_only=True, many=True)

    class Meta:
        model = ProductManager
        fields = ['product_option']


class ProductProductManagerSerializer(ModelSerializer):
    product_manager = ProductManagerProductOptionSerializer(read_only=True, many=True)
    category = CategoryMiniSerializer(many=True, read_only=True)

    class Meta:
        model = Product
        fields = ['product_manager', 'category']"""


class BrandDetailSerializer(BrandSerializer):
    pass
    # product = ProductProductManagerSerializer(many=True, read_only=True)


"""
Minified serializers.
"""
class BrandMiniSerializer(ModelSerializer):
    class Meta:
        model = Brand
        exclude = ['logo', 'value', 'created']
