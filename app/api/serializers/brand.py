# Django rest framework.
from rest_framework.serializers import ModelSerializer
from rest_framework.validators import UniqueValidator

# Models for serializers.
from shop.models.brand import *
from shop.models.product import Product, ProductManager, ProductOption


"""
One to one field serializers.
"""
class BrandBrandingSerializer(ModelSerializer):
    class Meta:
        model = BrandBranding
        fields = '__all__'
        read_only_fields = ['brand', 'logo']


class BrandBrandingLogoSerializer(ModelSerializer):
    class Meta:
        model = BrandBranding
        fields = ['id', 'logo']
        read_only_fields = ['id',]


class BrandImprintSerializer(ModelSerializer):
    class Meta:
        model = BrandImprint
        fields = '__all__'
        read_only_fields = ['brand']
        extra_kwargs = {
            'email': {'validators': [],},
            'phone': {'validators': [],},
            'tax_number': {'validators': [],},
            'line_1': {'validators': [], 'required': False,},
            'line_2': {'validators': [], 'required': False,},
            'post_code': {'validators': [], 'required': False,},
            'city': {'validators': [], 'required': False,},
            'country': {'validators': [], 'required': False,},
        }
        validators = []


"""
Manager (main) serializers.
"""
class BrandSerializer(ModelSerializer):
    branding = BrandBrandingSerializer()
    # imprint = BrandImprintSerializer()

    class Meta:
        model = Brand
        fields = '__all__'
        # depth=1

    def create(self, validated_data):
        branding_data = validated_data.pop('branding')
        # imprint_data = validated_data.pop('imprint')

        # New instance.
        instance = Brand.objects.create(**validated_data)

        # One to one fields.
        BrandBranding.objects.create(brand=instance, **branding_data)
        # BrandImprint.objects.create(brand=instance, **imprint_data)

        instance.save()
        return instance

    def update(self, instance, validated_data):
        branding_data = validated_data.pop('branding')

        # One to one fields.
        # BrandBranding.objects.update_or_create(brand=instance, defaults=branding_data)
        branding = BrandBrandingSerializer(instance=instance.branding, data=branding_data)
        if branding.is_valid():
            branding.save()

        # imprint = BrandImprintSerializer(brand=instance, data=imprint_data)
        # if imprint.is_valid():
        #     imprint.save()

        instance.save()
        return instance
