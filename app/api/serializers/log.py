from rest_framework.serializers import ModelSerializer

from shop.models.log import ValueLog


class ValueLogSerializer(ModelSerializer):

    class Meta:
        model = ValueLog
        fields = '__all__'
