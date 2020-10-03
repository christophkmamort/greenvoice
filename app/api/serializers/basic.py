from rest_framework.serializers import ModelSerializer

from shop.models.basic import BasicApi, BasicBanking, BasicImprint, \
                              BasicMetaData


"""
Universal serializers.
"""
class BasicApiSerializer(ModelSerializer):
    class Meta:
        model = BasicApi
        fields = '__all__'


class BasicMetaDataSerializer(ModelSerializer):
    class Meta:
        model = BasicMetaData
        fields = '__all__'


class BasicBankingSerializer(ModelSerializer):
    class Meta:
        model = BasicBanking
        fields = '__all__'


class BasicImprintSerializer(ModelSerializer):
    class Meta:
        model = BasicImprint
        fields = '__all__'
