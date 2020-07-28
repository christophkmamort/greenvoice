from rest_framework import serializers

from django.contrib.auth.models import User
from shop.models import Product


class ProductSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Product
        fields = ['id', 'title', 'image', 'price', 'status', 'created', 'owner']
        # fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    products = serializers.PrimaryKeyRelatedField(many=True, queryset=Product.objects.all())

    class Meta:
        model = User
        fields = ['id', 'username', 'products']
