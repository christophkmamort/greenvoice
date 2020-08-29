from rest_framework.serializers import ModelSerializer

from shop.models.media import ProductBrandImage, ProductImage


class ProductBrandImageSerializer(ModelSerializer):

    class Meta:
        model = ProductBrandImage
        fields = '__all__'


class ProductImageSerializer(ModelSerializer):

    class Meta:
        model = ProductImage
        fields = '__all__'
