from rest_framework.serializers import ModelSerializer

from .product import ProductDetailMiniSerializer
from .product_option import ProductOptionDetailMiniSerializer
from .taxonomies import ColorMiniSerializer
from shop.models.product import ProductManager, ProductOption
from shop.models.wishlist import WishlistItem


class WishlistItemSerializer(ModelSerializer):

    class Meta:
        model = WishlistItem
        fields = '__all__'


class WishlistProductManagerSerializer(ModelSerializer):
    product = ProductDetailMiniSerializer(read_only=True)
    color = ColorMiniSerializer(read_only=True)
    product_option = ProductOptionDetailMiniSerializer(many=True, read_only=True)

    class Meta:
        model = ProductManager
        exclude = ['query', 'value', 'created']


class WishlistItemDetailSerializer(ModelSerializer):
    product_manager = WishlistProductManagerSerializer(read_only=True)

    class Meta:
        model = WishlistItem
        fields = '__all__'
