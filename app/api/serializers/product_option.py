from rest_framework.serializers import ModelSerializer

from .product_manager import ProductManagerDetailSerializer
from .taxonomies import SizeMiniSerializer
from shop.models.product import ProductOption


class ProductOptionSerializer(ModelSerializer):

    class Meta:
        model = ProductOption
        fields = '__all__'


class ProductOptionDetailSerializer(ProductOptionSerializer):
    product_manager = ProductManagerDetailSerializer(read_only=True)
    size = SizeMiniSerializer(read_only=True)


class ProductOptionDetailMiniSerializer(ProductOptionSerializer):
    size = SizeMiniSerializer(read_only=True)

    class Meta:
        model = ProductOption
        exclude = ['value', 'created', 'product_manager']
