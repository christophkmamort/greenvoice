from rest_framework.serializers import ModelSerializer

from shop.models.brand import Brand
from shop.models.product import Product, ProductManager, ProductOption


"""
Basic brand serializer.
"""
class BrandSerializer(ModelSerializer):

    class Meta:
        model = Brand
        fields = '__all__'


"""
Brand detail serializer to check if brand is active
and has active products in stock.
"""
class ProductOptionStatusSerializer(ModelSerializer):

    class Meta:
        model = ProductOption
        fields = ['status']


class ProductManagerProductOptionSerializer(ModelSerializer):
    product_option = ProductOptionStatusSerializer(read_only=True, many=True)

    class Meta:
        model = ProductManager
        fields = ['product_option']


class ProductProductManagerSerializer(ModelSerializer):
    product_manager = ProductManagerProductOptionSerializer(read_only=True, many=True)

    class Meta:
        model = Product
        fields = ['product_manager']


class BrandDetailSerializer(BrandSerializer):
    product = ProductProductManagerSerializer(many=True, read_only=True)


"""
Minified brand serializer classes.
"""
class BrandMiniSerializer(ModelSerializer):

    class Meta:
        model = Brand
        exclude = ['logo', 'value', 'created']
