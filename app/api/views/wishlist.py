from rest_framework.viewsets import ModelViewSet

from api.serializers.wishlist import *
from api.permissions import IsUser
from shop.models.wishlist import *


class WishlistItemViewSet(ModelViewSet):
    """
    Manage `list`, `create`, `retrieve`, `update` and `destroy` wishlist items.
    """
    serializer_class = WishlistItemSerializer
    permission_classes = [IsUser]

    def get_queryset(self):
        return WishlistItem.objects.filter(customer=self.request.user.customer)

    def get_serializer_class(self):
        """
        Return appropriate serializer class for wishlist items.
        """
        if self.action == 'retrieve' or self.action == 'list':
            return WishlistItemDetailSerializer
        return self.serializer_class

    def perform_create(self, serializer):
        serializer.save(customer=self.request.user.customer)

    def perform_update(self, serializer):
        serializer.save(customer=self.request.user.customer)
