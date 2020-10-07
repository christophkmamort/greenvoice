from rest_framework.serializers import ModelSerializer

from .taxonomies.taxonomies import SizeMiniSerializer
from shop.models.product import ProductOption



"""
Basic serializers.
"""
class ProductOptionSerializer(ModelSerializer):

    class Meta:
        model = ProductOption
        fields = '__all__'



"""
Detail serializers.
"""
class ProductOptionDetailMiniSerializer(ProductOptionSerializer):
    size = SizeMiniSerializer(read_only=True)

    class Meta:
        model = ProductOption
        exclude = ['value', 'created', 'product_manager']


class ProductOptionStatusSerializer(ProductOptionSerializer):

    class Meta:
        model = ProductOption
        fields = ['status']
