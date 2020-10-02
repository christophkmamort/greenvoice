from rest_framework.serializers import ModelSerializer

from django.utils.text import slugify

from shop.models.meta_data import MetaDataCountry, MetaDataCompanyType, MetaDataCurrency
from taxonomies.models import *


"""
Category.
"""
class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class CategoryMiniSerializer(ModelSerializer):
    class Meta:
        model = Category
        exclude = ['slug', 'value', 'created']


class CategoryDetailMiniSerializer(CategoryMiniSerializer):
    parent = CategoryMiniSerializer(read_only=True)
    children = CategoryMiniSerializer(many=True, read_only=True)


"""
Color.
"""
class ColorSerializer(ModelSerializer):
    class Meta:
        model = Color
        fields = '__all__'


class ColorMiniSerializer(ModelSerializer):
    class Meta:
        model = Color
        exclude = ['slug', 'value', 'created']


"""
Country.
"""
class MetaDataCountrySerializer(ModelSerializer):
    class Meta:
        model = MetaDataCountry
        fields = '__all__'
        read_only_fields = ['taxonomy',]


class CountrySerializer(ModelSerializer):
    meta_data = MetaDataCountrySerializer()

    class Meta:
        model = Country
        fields = ['id', 'name', 'slug', 'meta_data']

    def create(self, validated_data):
        meta_data = validated_data.pop('meta_data')

        instance = Country.objects.create(**validated_data)
        instance.slug = slugify(validated_data.pop('name'))
        MetaDataCountry.objects.create(taxonomy=instance, **meta_data)

        instance.save()
        return instance

    def update(self, instance, validated_data):
        meta_data = validated_data.pop('meta_data')

        instance.name = validated_data.pop('name')
        instance.slug = slugify(instance.name)
        meta_data = MetaDataCountrySerializer(instance=instance.meta_data, data=meta_data)
        if meta_data.is_valid():
            meta_data.save()

        instance.save()
        return instance


"""
Company Type.
"""
class MetaDataCompanyTypeSerializer(ModelSerializer):
    class Meta:
        model = MetaDataCompanyType
        fields = '__all__'
        read_only_fields = ['taxonomy',]


class CompanyTypeSerializer(ModelSerializer):
    meta_data = MetaDataCompanyTypeSerializer()

    class Meta:
        model = CompanyType
        fields = ['id', 'name', 'slug', 'abbreviation', 'country', 'meta_data']
        read_only_fields = ['slug',]

    def create(self, validated_data):
        meta_data = validated_data.pop('meta_data')

        instance = CompanyType.objects.create(**validated_data)
        instance.slug = slugify(validated_data.pop('name'))
        MetaDataCompanyType.objects.create(taxonomy=instance, **meta_data)

        instance.save()
        return instance

    def update(self, instance, validated_data):
        meta_data = validated_data.pop('meta_data')

        instance.abbreviation = validated_data.pop('abbreviation')
        instance.country = validated_data.pop('country')
        instance.name = validated_data.pop('name')
        instance.slug = slugify(instance.name)
        meta_data = MetaDataCurrencySerializer(instance=instance.meta_data, data=meta_data)
        if meta_data.is_valid():
            meta_data.save()

        instance.save()
        return instance


"""
Currency.
"""
class MetaDataCurrencySerializer(ModelSerializer):
    class Meta:
        model = MetaDataCurrency
        fields = '__all__'
        read_only_fields = ['taxonomy',]


class CurrencySerializer(ModelSerializer):
    meta_data = MetaDataCurrencySerializer()

    class Meta:
        model = Currency
        fields = ['id', 'name', 'slug', 'code_iso_4217', 'symbol', 'countries', 'meta_data']
        read_only_fields = ['slug',]

    def create(self, validated_data):
        countries = validated_data.pop('countries')
        meta_data = validated_data.pop('meta_data')

        instance = Currency.objects.create(**validated_data)
        instance.countries.set(countries)
        instance.slug = slugify(validated_data.pop('name'))
        MetaDataCurrency.objects.create(taxonomy=instance, **meta_data)

        instance.save()
        return instance

    def update(self, instance, validated_data):
        instance.code_iso_4217 = validated_data.pop('code_iso_4217')
        instance.countries.set(validated_data.pop('countries'))
        instance.name = validated_data.pop('name')
        instance.slug = slugify(instance.name)
        instance.symbol = validated_data.pop('symbol')
        meta_data = MetaDataCurrencySerializer(instance=instance.meta_data, data=validated_data.pop('meta_data'))
        if meta_data.is_valid():
            meta_data.save()

        instance.save()
        return instance


"""
Size.
"""
class SizeSerializer(ModelSerializer):
    class Meta:
        model = Size
        fields = '__all__'


class SizeMiniSerializer(ModelSerializer):
    class Meta:
        model = Size
        exclude = ['slug', 'value', 'created', 'order']


"""
Target Group.
"""
class TargetGroupSerializer(ModelSerializer):
    class Meta:
        model = TargetGroup
        fields = '__all__'


class TargetGroupMiniSerializer(ModelSerializer):
    class Meta:
        model = TargetGroup
        exclude = ['slug', 'value', 'created']
