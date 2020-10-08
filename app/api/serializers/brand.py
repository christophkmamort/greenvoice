# Django rest framework.
from rest_framework.serializers import CharField, EmailField, \
                                       ModelSerializer # , PrimaryKeyRelatedField
from rest_framework.validators import UniqueValidator

# Models for serializers.
from shop.models.brand import *
from shop.models.product import Product, ProductManager, ProductOption
from shop.models.basic_with_relations import BasicTax

# One to one field serializers.
from .basic import BasicApiSerializer, BasicBankingSerializer, \
                   BasicMetaDataSerializer, BasicTaxSerializer

# Other.
# from .product_option import ProductOptionStatusSerializer
# from .taxonomies import CategoryMiniSerializer


"""
One to one field serializers.
"""
class BrandBrandingSerializer(ModelSerializer):
    class Meta:
        model = BrandBranding
        exclude = ['brand',]


class BrandImprintSerializer(ModelSerializer):
    class Meta:
        model = BrandImprint
        exclude = ['brand',]
        extra_kwargs = {
            'email': {'validators': [],},
            'phone': {'validators': [],},
            'tax_number': {'validators': [],},
        }


"""
Main serializer.
"""
class BrandSerializer(ModelSerializer):
    branding = BrandBrandingSerializer()
    imprint = BrandImprintSerializer()

    class Meta:
        model = Brand
        fields = '__all__'

    def create(self, validated_data):
        branding_data = validated_data.pop('branding')
        imprint_data = validated_data.pop('imprint')

        # Create new instance.
        instance = Brand.objects.create(**validated_data)

        # One to one fields.
        BrandBranding.objects.create(brand=instance, **branding_data)
        BrandImprint.objects.create(brand=instance, **imprint_data)

        instance.save()
        return instance

    def update(self, instance, validated_data):
        # TODO: Add unique check here!!

        # One to one fields.
        BrandBranding.objects.update_or_create(brand=instance, defaults=validated_data.pop('branding'))
        BrandImprint.objects.update_or_create(brand=instance, defaults=validated_data.pop('imprint'))

        instance.save()
        return instance


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
