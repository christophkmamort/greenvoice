from rest_framework.serializers import ModelSerializer

from shop.models.product import Product, ProductManager, ProductOption


class ProductSerializer(ModelSerializer):

    class Meta:
        model = Product
        exclude = ['query', 'value',]


class ProductManagerSerializer(ModelSerializer):

    class Meta:
        model = ProductManager
        exclude = ['value',]


class ProductOptionSerializer(ModelSerializer):

    class Meta:
        model = ProductOption
        exclude = ['value',]
