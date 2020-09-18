from rest_framework.serializers import ModelSerializer, PrimaryKeyRelatedField

from .media import ProductBrandImageSerializer, ProductImageSerializer
from .product import ProductDetailMiniSerializer
from .taxonomies import ColorMiniSerializer, SizeMiniSerializer
from shop.models.product import ProductManager, ProductOption


class ProductManagerSerializer(ModelSerializer):

    class Meta:
        model = ProductManager
        fields = '__all__'


class ProductOptionDetailMiniSerializer(ModelSerializer):
    size = SizeMiniSerializer(read_only=True)

    class Meta:
        model = ProductOption
        exclude = ['value', 'created', 'product_manager']


class ProductManagerDetailSerializer(ProductManagerSerializer):
    color = ColorMiniSerializer(read_only=True)
    product = ProductDetailMiniSerializer(read_only=True)
    product_option = ProductOptionDetailMiniSerializer(read_only=True, many=True)
    image = ProductImageSerializer(read_only=True, many=True)
    brand_image = ProductBrandImageSerializer(read_only=True, many=True)
    wishlist_item = PrimaryKeyRelatedField(many=True, read_only=True)
