from rest_framework.serializers import ModelSerializer

from .product import ProductDetailMiniSerializer
from .taxonomies import ColorMiniSerializer, SizeMiniSerializer
from shop.models.order import *
from shop.models.product import ProductManager, ProductOption


class OrderSerializer(ModelSerializer):

    class Meta:
        model = Order
        fields = '__all__'
        read_only_fields = ['customer',]


class OrderItemSerializer(ModelSerializer):

    class Meta:
        model = OrderItem
        fields = '__all__'
        read_only_fields = ['customer',]


class OrderProductManagerSerializer(ModelSerializer):
    product = ProductDetailMiniSerializer(read_only=True)
    color = ColorMiniSerializer(read_only=True)

    class Meta:
        model = ProductManager
        exclude = ['query', 'value', 'created']


class OrderProductOptionSerializer(ModelSerializer):
    product_manager = OrderProductManagerSerializer(read_only=True)
    size = SizeMiniSerializer(read_only=True)

    class Meta:
        model = ProductOption
        exclude = ['value', 'created']


class OrderItemDetailSerializer(OrderItemSerializer):
    product_option = OrderProductOptionSerializer(read_only=True)


class OrderDetailSerializer(OrderSerializer):
    order_items = OrderItemDetailSerializer(many=True, read_only=True)
