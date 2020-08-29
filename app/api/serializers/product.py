from rest_framework.serializers import ModelSerializer

from shop.models.product import Product, ProductManager, ProductOption


class ProductSerializer(ModelSerializer):

    class Meta:
        model = Product
        fields = '__all__'


class ProductManagerSerializer(ModelSerializer):

    class Meta:
        model = ProductManager
        fields = '__all__'


class ProductOptionSerializer(ModelSerializer):

    class Meta:
        model = ProductOption
        fields = '__all__'
