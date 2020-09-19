from rest_framework.serializers import ModelSerializer

from .product_manager import ProductManagerDetailForWishlistSerializer
from shop.models.wishlist import WishlistItem


"""
Basic serializers.
"""
class WishlistItemSerializer(ModelSerializer):

    class Meta:
        model = WishlistItem
        fields = '__all__'
        read_only_fields = ['customer',]


"""
Detail serializers.
"""
class WishlistItemDetailSerializer(WishlistItemSerializer):
    product_manager = ProductManagerDetailForWishlistSerializer(read_only=True)
