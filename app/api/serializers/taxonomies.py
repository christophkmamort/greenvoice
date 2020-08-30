from rest_framework.serializers import ModelSerializer

from shop.models.taxonomies import Category, Color, Size, UserGroup


class CategorySerializer(ModelSerializer):

    class Meta:
        model = Category
        fields = '__all__'


class ColorSerializer(ModelSerializer):

    class Meta:
        model = Color
        fields = '__all__'


class SizeSerializer(ModelSerializer):

    class Meta:
        model = Size
        fields = '__all__'


class UserGroupSerializer(ModelSerializer):

    class Meta:
        model = UserGroup
        fields = '__all__'
