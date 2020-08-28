from rest_framework.serializers import ModelSerializer

from shop.models.product import Product, ProductOption


class ProductOptionSerializer(ModelSerializer):

    class Meta:
        model = ProductOption
        fields = '__all__'


class ProductSerializer(ModelSerializer):
    # brand = BrandSerializer()

    class Meta:
        model = Product
        fields = '__all__'
