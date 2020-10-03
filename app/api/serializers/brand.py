# Django rest framework.
from rest_framework.serializers import ModelSerializer

# Models for serializers.
from shop.models.brand import Brand, BrandBranding, BrandSettings, \
                                BrandSalesSettings
from shop.models.product import Product, ProductManager, ProductOption
from shop.models.basic import BasicTax

# One to one field serializers.
from .basic import BasicApiSerializer, BasicBankingSerializer, \
                        BasicImprintSerializer, BasicMetaDataSerializer

# Other.
# from .product_option import ProductOptionStatusSerializer
# from .taxonomies import CategoryMiniSerializer

"""
One to one field serializers.
"""
class BrandBrandingSerializer(ModelSerializer):
    class Meta:
        model = BrandBranding
        fields = '__all__'


class BrandSettingsSerializer(ModelSerializer):
    class Meta:
        model = BrandSettings
        fields = '__all__'


class BasicTaxSerializer(ModelSerializer):
    class Meta:
        model = BasicTax
        fields = '__all__'


"""
Main serializer.
"""
class BrandSerializer(ModelSerializer):
    api = BasicApiSerializer()
    branding = BrandBrandingSerializer()
    banking = BasicBankingSerializer()
    imprint = BasicImprintSerializer()
    meta_data = BasicMetaDataSerializer()
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
