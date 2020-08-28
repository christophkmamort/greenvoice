from rest_framework.serializers import ModelSerializer

from shop.models.brand import Brand


class BrandSerializer(ModelSerializer):

    class Meta:
        model = Brand
        exclude = ['created',]
