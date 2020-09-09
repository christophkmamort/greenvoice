from rest_framework.serializers import ModelSerializer

from taxonomies.models import *


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
