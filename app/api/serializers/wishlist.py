from rest_framework.serializers import ModelSerializer

from .product import ProductManagerSerializer
from shop.models.wishlist import WishlistItem


class WishlistItemSerializer(ModelSerializer):

    class Meta:
        model = WishlistItem
        fields = '__all__'


class WishlistItemDetailSerializer(ModelSerializer):
    product_manager = ProductManagerSerializer(read_only=True)

    class Meta:
        model = WishlistItem
        fields = '__all__'
