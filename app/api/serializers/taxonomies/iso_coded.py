from rest_framework.serializers import ModelSerializer

from django.utils.text import slugify

from taxonomies.models.iso_coded import *


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

        # Instance.
        instance = Country.objects.create(**validated_data)
        instance.slug = slugify(validated_data.pop('name'))

        # One to one fields.
        MetaDataCountry.objects.create(taxonomy=instance, **meta_data)

        instance.save()
        return instance

    def update(self, instance, validated_data):
        meta_data = validated_data.pop('meta_data')

        # Instance.
        instance = Country.objects.update_or_create(id=instance.id, defaults=validated_data)[0]
        instance.slug = slugify(validated_data.pop('name'))

        # One to one fields.
        MetaDataCountry.objects.update_or_create(taxonomy=instance, defaults=meta_data)

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

        # Instance.
        instance = CompanyType.objects.create(**validated_data)
        instance.slug = slugify(validated_data.pop('name'))

        # One to one fields.
        MetaDataCompanyType.objects.create(taxonomy=instance, **meta_data)

        instance.save()
        return instance

    def update(self, instance, validated_data):
        meta_data = validated_data.pop('meta_data')

        # Instance.
        instance = CompanyType.objects.update_or_create(id=instance.id, defaults=validated_data)[0]
        instance.slug = slugify(validated_data.pop('name'))

        # One to one fields.
        MetaDataCompanyType.objects.update_or_create(taxonomy=instance, defaults=meta_data)

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

        # Instance.
        instance = Currency.objects.create(**validated_data)
        instance.slug = slugify(validated_data.pop('name'))

        # Many to many fields.
        instance.countries.set(countries)
        # One to one fields.
        MetaDataCurrency.objects.create(taxonomy=instance, **meta_data)

        instance.save()
        return instance

    def update(self, instance, validated_data):
        countries = validated_data.pop('countries')
        meta_data = validated_data.pop('meta_data')

        # Instance.
        instance = Currency.objects.update_or_create(id=instance.id, defaults=validated_data)[0]
        instance.slug = slugify(validated_data.pop('name'))

        # Many to many fields.
        instance.countries.set(countries)
        # One to one fields.
        MetaDataCurrency.objects.update_or_create(taxonomy=instance, defaults=meta_data)

        instance.save()
        return instance
