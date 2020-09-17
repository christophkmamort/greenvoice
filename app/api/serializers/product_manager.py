from rest_framework.serializers import ModelSerializer, PrimaryKeyRelatedField

from .media import ProductBrandImageSerializer, ProductImageSerializer
from .taxonomies import ColorSerializer, SizeSerializer
from shop.models.product import Product, ProductManager, ProductOption


class ProductManagerSerializer(ModelSerializer):

    class Meta:
        model = ProductManager
        fields = '__all__'


class ProductDetailSerializer(ModelSerializer):

    class Meta:
        model = Product
        fields = '__all__'


class ProductOptionDetailSerializer(ModelSerializer):

    class Meta:
        model = ProductOption
        fields = '__all__'


class ProductManagerDetailSerializer(ProductManagerSerializer):
    color = ColorSerializer(read_only=True)
    product = ProductDetailSerializer(read_only=True)
    product_option = ProductOptionDetailSerializer(read_only=True, many=True)
    image = ProductImageSerializer(read_only=True, many=True)
    brand_image = ProductBrandImageSerializer(read_only=True, many=True)
    # wishlist_item = PrimaryKeyRelatedField(many=True, read_only=True)
