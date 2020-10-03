from rest_framework.serializers import ModelSerializer

from shop.models.basic import BasicApi, BasicBanking, BasicImprint, \
                              BasicMetaData, BasicTax, BasicTaxZones


"""
Universal serializers.
"""
class BasicApiSerializer(ModelSerializer):
    class Meta:
        model = BasicApi
        fields = '__all__'


class BasicBankingSerializer(ModelSerializer):
    class Meta:
        model = BasicBanking
        fields = '__all__'


class BasicImprintSerializer(ModelSerializer):
    class Meta:
        model = BasicImprint
        fields = '__all__'


class BasicMetaDataSerializer(ModelSerializer):
    class Meta:
        model = BasicMetaData
        fields = '__all__'


class BasicTaxZonesSerializer(ModelSerializer):
    class Meta:
        model = BasicTaxZones
        fields = '__all__'


class BasicTaxSerializer(ModelSerializer):
    tax_zones = BasicTaxZonesSerializer(many=True,)

    class Meta:
        model = BasicTax
        fields = '__all__'
