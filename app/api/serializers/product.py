from rest_framework.serializers import ModelSerializer

from .brand import BrandMiniSerializer
from .taxonomies import CategoryMiniSerializer, TargetGroupMiniSerializer
from shop.models.product import Product



"""
Basic serializers.
"""
class ProductSerializer(ModelSerializer):

    class Meta:
        model = Product
        fields = '__all__'



"""
Detail serializers.
"""
class ProductDetailSerializer(ProductSerializer):
    brand = BrandMiniSerializer(read_only=True)
    target_group = TargetGroupMiniSerializer(many=True, read_only=True)
    category = CategoryMiniSerializer(many=True, read_only=True)


class ProductDetailMiniSerializer(ProductSerializer):
    brand = BrandMiniSerializer(read_only=True)
    target_group = TargetGroupMiniSerializer(many=True, read_only=True)
    category = CategoryMiniSerializer(many=True, read_only=True)

    class Meta:
        model = Product
        exclude = ['value', 'created']
