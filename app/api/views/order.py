# from url_filter.integrations.drf import DjangoFilterBackend

from rest_framework.filters import OrderingFilter
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from api.serializers.order import *
from shop.models.order import *


class OrderViewSet(ModelViewSet):
    """
    Manage `list`, `create`, `retrieve`, `update` and `destroy`.
    """
    filter_backends = [OrderingFilter] # DjangoFilterBackend
    # filter_fields = ['order_items']
    ordering_fields = ['created']
    ordering = ['-created']
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated] # TODO: IsUserOrStaff

    def get_queryset(self): # TODO: Check if works without this.
        return Order.objects.filter(customer=self.request.user.customer)

    def get_serializer_class(self):
        if self.action == 'retrieve' or self.action == 'list':
            return OrderDetailSerializer
        return self.serializer_class

    def perform_create(self, serializer):
        serializer.save(customer=self.request.user.customer)

    def perform_update(self, serializer):
        serializer.save(customer=self.request.user.customer)


class OrderItemViewSet(ModelViewSet):
    """
    Manage `list`, `create`, `retrieve`, `update` and `destroy`.
    """
    filter_backends = [OrderingFilter]
    ordering_fields = ['created']
    ordering = ['-created']
    serializer_class = OrderItemSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self): # TODO: Check if works without this.
        return OrderItem.objects.filter(customer=self.request.user.customer)

    def get_serializer_class(self):
        if self.action == 'retrieve' or self.action == 'list':
            return OrderItemDetailSerializer
        return self.serializer_class

    def perform_create(self, serializer):
        serializer.save(customer=self.request.user.customer)

    def perform_update(self, serializer):
        serializer.save(customer=self.request.user.customer)
