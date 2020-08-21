from rest_framework.serializers import HyperlinkedModelSerializer, PrimaryKeyRelatedField, ModelSerializer, HyperlinkedIdentityField, StringRelatedField, HyperlinkedRelatedField

from shop.models.customer import Customer
from shop.models.brand import Brand
from shop.models.product import Product
from shop.models.order import Order, OrderItem
from users.models import CustomUser


class ProductSerializer(HyperlinkedModelSerializer):
    # owner = ReadOnlyField(source='owner.username')
    brand = PrimaryKeyRelatedField(many=False, queryset=Brand.objects.all())

    class Meta:
        model = Product
        fields = '__all__'


class UserSerializer(HyperlinkedModelSerializer):
    # products = PrimaryKeyRelatedField(many=True, queryset=Product.objects.all())

    class Meta:
        model = CustomUser
        fields = ['url', 'last_login', 'is_superuser', 'email', 'is_staff', 'is_active', 'date_joined', 'user_permissions']


class CustomerSerializer(ModelSerializer):
    # products = PrimaryKeyRelatedField(many=True, queryset=Product.objects.all())

    class Meta:
        model = Customer
        fields = '__all__'


class OrderItemSerializer(ModelSerializer): # HyperlinkedModelSerializer
    # url = HyperlinkedIdentityField(view_name='order-item-detail')
    # owner = ReadOnlyField(source='owner.username')
    # order = PrimaryKeyRelatedField(many=False, queryset=Order.objects.all())
    product = ProductSerializer()

    class Meta:
        model = OrderItem
        fields = '__all__'


class OrderSerializer(ModelSerializer): # HyperlinkedModelSerializer
    url = HyperlinkedIdentityField(view_name='order-detail')
    customer = CustomerSerializer(many=False)
    items = OrderItemSerializer(many=True)

    class Meta:
        model = Order
        fields = '__all__'

    """def get_customer(self, obj):
        return str(obj.customer.name)"""

    """def get_order_items(self, obj):
        content_type = obj.get_content_type
        object_id = obj.id
        oi_qs = OrderItem.objects.filter_by_instance(obj)
        order_items = OrderItemSerializer(oi_qs, many=True).data
        return order_items"""

    def create(self, validated_data):
        order_items_data = validated_data.pop('order_items')
        order = Order.objects.create(**validated_data)
        for order_item_data in order_items_data:
            OrderItem.objects.create(order=order, **order_item_data)
        return order
