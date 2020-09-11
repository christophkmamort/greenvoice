from rest_framework.serializers import ModelSerializer, PrimaryKeyRelatedField

from .media import ProductBrandImageSerializer, ProductImageSerializer
from .taxonomies import ColorSerializer, SizeSerializer
from shop.models.product import Product, ProductManager, ProductOption


class ProductSerializer(ModelSerializer):

    class Meta:
        model = Product
        fields = '__all__'


class ProductManagerSerializer(ModelSerializer):
    product = ProductSerializer(read_only=True)

    class Meta:
        model = ProductManager
        fields = '__all__'


class ProductOptionSerializer(ModelSerializer):

    class Meta:
        model = ProductOption
        fields = '__all__'


class ProductOptionDetailSerializer(ModelSerializer):
    size = SizeSerializer(read_only=True)

    class Meta:
        model = ProductOption
        fields = '__all__'


class ProductManagerDetailSerializer(ModelSerializer):
    color = ColorSerializer(read_only=True)
    product = ProductSerializer(read_only=True)
    product_option = ProductOptionDetailSerializer(read_only=True, many=True)
    image = ProductImageSerializer(read_only=True, many=True)
    brand_image = ProductBrandImageSerializer(read_only=True, many=True)
    wishlist_item = PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = ProductManager
        fields = '__all__'
        # fields = ['id', 'color', 'product', 'product_option', 'image', 'brand_image', 'query', 'value', 'created', 'wishlist_item']
