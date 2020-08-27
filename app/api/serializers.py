from rest_framework.serializers import ModelSerializer, SerializerMethodField, \
                                    HyperlinkedModelSerializer

from shop.models.brand import Brand
from shop.models.customer import Customer
from shop.models.log import ValueLog
from shop.models.product import Product
from shop.models.order import Order, OrderItem
from shop.models.taxonomies import Category
from users.models import CustomUser


class ValueLogSerializer(ModelSerializer):

    class Meta:
        model = ValueLog
        fields = '__all__'


class BrandSerializer(ModelSerializer):

    class Meta:
        model = Brand
        exclude = ['created',]


class CategorySerializer(ModelSerializer):

    class Meta:
        model = Category
        fields = '__all__'


class ProductSerializer(ModelSerializer):
    # brand = BrandSerializer()

    class Meta:
        model = Product
        fields = '__all__'


class UserSerializer(ModelSerializer):

    class Meta:
        model = CustomUser
        fields = ['url', 'last_login', 'is_superuser', 'email', 'is_staff', 'is_active', 'date_joined', 'user_permissions',]


class CustomerSerializer(ModelSerializer):

    class Meta:
        model = Customer
        fields = '__all__'


class OrderItemSerializer(ModelSerializer):

    class Meta:
        model = OrderItem
        exclude = ['customer',]
        read_only_fields = ['id',]


class OrderItemDetailSerializer(OrderItemSerializer):
    product = ProductSerializer(read_only=True)


class OrderSerializer(ModelSerializer):
    items = SerializerMethodField()

    class Meta:
        model = Order
        fields = '__all__'
        read_only_fields = ['id', 'customer',]

    def get_items(self, obj):
        queryset = OrderItem.objects.filter(order=obj.id)
        items = OrderItemDetailSerializer(queryset, many=True).data
        return items

    """def create(self, validated_data):
        items_data = validated_data.pop('items')
        order = Order.objects.create(**validated_data)
        for order_item_data in items_data:
            OrderItem.objects.create(order=order, **order_item_data)
        return order"""
