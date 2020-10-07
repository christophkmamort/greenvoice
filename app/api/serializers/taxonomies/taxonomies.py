from rest_framework.serializers import ModelSerializer

from django.utils.text import slugify

from taxonomies.models import *


"""
Category.
"""
class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class CategoryMiniSerializer(ModelSerializer):
    class Meta:
        model = Category
        exclude = ['slug', 'value', 'created']


class CategoryDetailMiniSerializer(CategoryMiniSerializer):
    parent = CategoryMiniSerializer(read_only=True)
    children = CategoryMiniSerializer(many=True, read_only=True)


"""
Color.
"""
class ColorSerializer(ModelSerializer):
    class Meta:
        model = Color
        fields = '__all__'


class ColorMiniSerializer(ModelSerializer):
    class Meta:
        model = Color
        exclude = ['slug', 'value', 'created']


"""
Size.
"""
class SizeSerializer(ModelSerializer):
    class Meta:
        model = Size
        fields = '__all__'


class SizeMiniSerializer(ModelSerializer):
    class Meta:
        model = Size
        exclude = ['slug', 'value', 'created', 'order']


"""
Target Group.
"""
class TargetGroupSerializer(ModelSerializer):
    class Meta:
        model = TargetGroup
        fields = '__all__'


class TargetGroupMiniSerializer(ModelSerializer):
    class Meta:
        model = TargetGroup
        exclude = ['slug', 'value', 'created']
