from rest_framework.serializers import ModelSerializer

from users.models.customer import Customer
from users.models import CustomUser


class UserSerializer(ModelSerializer):

    class Meta:
        model = CustomUser
        fields = '__all__'


class CustomerSerializer(ModelSerializer):

    class Meta:
        model = Customer
        fields = '__all__'
