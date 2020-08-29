from rest_framework.serializers import ModelSerializer

from shop.models.taxonomies import Category, Color, Size, UserGroup


class CategorySerializer(ModelSerializer):

    class Meta:
        model = Category
        exclude = ['slug', 'value',]


class ColorSerializer(ModelSerializer):

    class Meta:
        model = Color
        exclude = ['slug', 'value',]


class SizeSerializer(ModelSerializer):

    class Meta:
        model = Size
        exclude = ['slug', 'value',]


class UserGroupSerializer(ModelSerializer):

    class Meta:
        model = UserGroup
        exclude = ['slug', 'value',]
