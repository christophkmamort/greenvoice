from rest_framework.serializers import ModelSerializer, SerializerMethodField

from .product_manager import ProductManagerDetailForOrderSerializer
from .product import ProductDetailMiniSerializer
from .taxonomies import ColorMiniSerializer, SizeMiniSerializer
from shop.models.order import *
from shop.models.product import ProductManager, ProductOption


"""
Basic order + order-item serializer.
"""
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


"""
Order + order-item detail serializer to get all required data and
check if brand is active and has active products in stock.
"""
class ProductOrderDetailForOrderSerializer(ModelSerializer):
    product_manager = ProductManagerDetailForOrderSerializer(read_only=True)
    size = SizeMiniSerializer(read_only=True)

    class Meta:
        model = ProductOption
        exclude = ['value', 'created']


class OrderItemDetailSerializer(OrderItemSerializer):
    product_option = ProductOrderDetailForOrderSerializer(read_only=True)


class OrderDetailSerializer(OrderSerializer):
    order_items = SerializerMethodField()

    def get_order_items(self, instance):
        order_items = instance.order_items.order_by('created')
        return OrderItemDetailSerializer(order_items, many=True, read_only=True).data
