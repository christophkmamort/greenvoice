from rest_framework.serializers import ModelSerializer

from shop.models.log import BrandValueLog, ProductValueLog, TaxonomyValueLog


class BrandValueLogSerializer(ModelSerializer):

    class Meta:
        model = BrandValueLog
        fields = '__all__'


class ProductValueLogSerializer(ModelSerializer):

    class Meta:
        model = ProductValueLog
        fields = '__all__'


class TaxonomyValueLogSerializer(ModelSerializer):

    class Meta:
        model = TaxonomyValueLog
        fields = '__all__'
