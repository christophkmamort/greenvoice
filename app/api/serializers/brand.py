from rest_framework.serializers import ModelSerializer

from .product import ProductDetailSerializer
from shop.models.brand import Brand


class BrandSerializer(ModelSerializer):

    class Meta:
        model = Brand
        fields = '__all__'


class BrandDetailSerializer(BrandSerializer):
    product = ProductDetailSerializer(many=True, read_only=True)
