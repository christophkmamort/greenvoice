# Django rest framework.
from rest_framework.serializers import CharField, EmailField, \
                                       ModelSerializer # , PrimaryKeyRelatedField
from rest_framework.validators import UniqueValidator

# Models for serializers.
# from shop.models.basic import BasicApi, BasicBanking, BasicTax, BasicTaxZones
from shop.models.brand import Brand, BrandImprint # , BrandBranding, BrandPerson, BrandSettings, BrandSettingsSales, BrandSettingsStatus
from shop.models.product import Product, ProductManager, ProductOption
from shop.models.basic import BasicTax

# One to one field serializers.
from .basic import BasicApiSerializer, BasicBankingSerializer, \
                   BasicMetaDataSerializer, BasicTaxSerializer

# Other.
# from .product_option import ProductOptionStatusSerializer
# from .taxonomies import CategoryMiniSerializer


"""
One to one field serializers.
"""
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
    imprint = BrandImprintSerializer()

    class Meta:
        model = Brand
        fields = '__all__'

    def create(self, validated_data):
        imprint = validated_data.pop('imprint')
        instance = Brand.objects.create(**validated_data)
        BrandImprint.objects.create(brand=instance) # , **imprint

        instance.save()
        return instance

    def update(self, instance, validated_data):
        """ imprint = validated_data.pop('imprint')
        imprint['company_type'] = imprint['company_type'].pk
        imprint['country'] = imprint['country'].pk

        imprint = BrandImprintSerializer(instance=instance.imprint, data=imprint)
        if imprint.is_valid():
            # TODO: Add uniquness check.
            # TODO: Check django objects.update() method.
            imprint.save() """

        imprint = BrandImprint.objects.update_or_create(brand=instance, defaults=validated_data.pop('imprint'))

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
