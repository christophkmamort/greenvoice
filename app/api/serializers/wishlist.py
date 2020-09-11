from rest_framework.serializers import ModelSerializer

from shop.models.wishlist import WishlistItem


class WishlistItemSerializer(ModelSerializer):

    class Meta:
        model = WishlistItem
        fields = '__all__'
