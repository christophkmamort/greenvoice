from rest_framework.serializers import ModelSerializer

from shop.models.product import Product, ProductManager, ProductOption


class ProductSerializer(ModelSerializer):

    class Meta:
        model = Product
        fields = '__all__'


class ProductOptionDetailSerializer(ModelSerializer):

    class Meta:
        model = ProductOption
        fields = '__all__'


class ProductManagerDetailSerializer(ModelSerializer):
    product_option = ProductOptionDetailSerializer(many=True, read_only=True)

    class Meta:
        model = ProductManager
        fields = '__all__'


class ProductDetailSerializer(ProductSerializer):
    product_manager = ProductManagerDetailSerializer(many=True, read_only=True)





"""class ProductOptionSerializer(ModelSerializer):

    class Meta:
        model = ProductOption
        fields = '__all__'


class ProductManagerOptionDetailSerializer(ProductManagerSerializer):
    color = ColorSerializer(read_only=True)
    product = ProductSerializer(read_only=True)
    image = ProductImageSerializer(read_only=True, many=True)
    brand_image = ProductBrandImageSerializer(read_only=True, many=True)


class ProductManagerWishlistDetailSerializer(ProductManagerSerializer):
    product = ProductSerializer(read_only=True)
    product_option = ProductOptionSerializer(read_only=True, many=True)
    image = ProductImageSerializer(read_only=True, many=True)
    brand_image = ProductBrandImageSerializer(read_only=True, many=True)"""


"""class ProductOptionDetailSerializer(ProductOptionSerializer):
    product_manager = ProductManagerOptionDetailSerializer(read_only=True)
    size = SizeSerializer(read_only=True)"""
