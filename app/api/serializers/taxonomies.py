from rest_framework.serializers import ModelSerializer

from taxonomies.models import *


"""
Basic serializers.
"""
class CategorySerializer(ModelSerializer):

    class Meta:
        model = Category
        fields = '__all__'


class ColorSerializer(ModelSerializer):

    class Meta:
        model = Color
        fields = '__all__'


class CountrySerializer(ModelSerializer):

    class Meta:
        model = Country
        fields = '__all__'


class SizeSerializer(ModelSerializer):

    class Meta:
        model = Size
        fields = '__all__'


class TargetGroupSerializer(ModelSerializer):

    class Meta:
        model = TargetGroup
        fields = '__all__'


"""
Minified serializers.
"""
class CategoryMiniSerializer(ModelSerializer):

    class Meta:
        model = Category
        exclude = ['slug', 'value', 'created']


class ColorMiniSerializer(ModelSerializer):

    class Meta:
        model = Color
        exclude = ['slug', 'value', 'created']


class SizeMiniSerializer(ModelSerializer):

    class Meta:
        model = Size
        exclude = ['slug', 'value', 'created', 'order']


class TargetGroupMiniSerializer(ModelSerializer):

    class Meta:
        model = TargetGroup
        exclude = ['slug', 'value', 'created']
