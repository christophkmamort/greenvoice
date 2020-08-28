from rest_framework.serializers import ModelSerializer

from shop.models.gallery import ProductBrandImage, ProductImage


class ProductBrandGallerySerializer(ModelSerializer):

    class Meta:
        model = ProductBrandImage
        fields = '__all__'


class ProductGallerySerializer(ModelSerializer):

    class Meta:
        model = ProductImage
        fields = '__all__'
