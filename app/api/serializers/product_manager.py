from rest_framework.serializers import ModelSerializer, PrimaryKeyRelatedField

from .media import ProductBrandImageSerializer, ProductImageSerializer
from .product_option import ProductOptionDetailMiniSerializer
from .product import ProductDetailMiniSerializer
from .taxonomies import ColorMiniSerializer
from shop.models.product import ProductManager, ProductOption


"""
Basic serializers.
"""
class ProductManagerSerializer(ModelSerializer):

    class Meta:
        model = ProductManager
        fields = '__all__'


"""
Detail serializers.
"""
class ProductManagerDetailSerializer(ProductManagerSerializer):
    color = ColorMiniSerializer(read_only=True)
    product = ProductDetailMiniSerializer(read_only=True)
    product_option = ProductOptionDetailMiniSerializer(read_only=True, many=True)
    image = ProductImageSerializer(read_only=True, many=True)
    brand_image = ProductBrandImageSerializer(read_only=True, many=True)
    wishlist_item = PrimaryKeyRelatedField(many=True, read_only=True)


class ProductManagerDetailForWishlistSerializer(ProductManagerSerializer):
    product = ProductDetailMiniSerializer(read_only=True)
    color = ColorMiniSerializer(read_only=True)
    product_option = ProductOptionDetailMiniSerializer(many=True, read_only=True)

    class Meta:
        model = ProductManager
        exclude = ['query', 'value', 'created']


class ProductManagerDetailForOrderSerializer(ProductManagerSerializer):
    product = ProductDetailMiniSerializer(read_only=True)
    color = ColorMiniSerializer(read_only=True)

    class Meta:
        model = ProductManager
        exclude = ['query', 'value', 'created']
