from rest_framework.serializers import ModelSerializer, SerializerMethodField

from .product import ProductOptionDetailSerializer
from shop.models.order import *


class OrderItemSerializer(ModelSerializer):

    class Meta:
        model = OrderItem
        fields = '__all__'


class OrderItemDetailSerializer(OrderItemSerializer):
    product_option = ProductOptionDetailSerializer(read_only=True)


class OrderSerializer(ModelSerializer):

    class Meta:
        model = Order
        fields = '__all__'
        read_only_fields = ['customer',]

    """ def get_items(self, obj):
        queryset = OrderItem.objects.filter(order=obj.id)
        items = OrderItemDetailSerializer(queryset, many=True).data
        return items """

    """ def create(self, validated_data):
        items_data = validated_data.pop('items')
        order = Order.objects.create(**validated_data)
        for order_item_data in items_data:
            OrderItem.objects.create(order=order, **order_item_data)
        return order """


class OrderDetailSerializer(OrderSerializer):
    order_items = OrderItemDetailSerializer(many=True, read_only=True)
