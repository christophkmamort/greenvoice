from rest_framework.serializers import ModelSerializer

from users.models.customer import Customer
from users.models import CustomUser


class CustomerSerializer(ModelSerializer):

    class Meta:
        model = Customer
        fields = '__all__'


class UserSerializer(ModelSerializer):

    class Meta:
        model = CustomUser
        fields = '__all__'


class CustomerDetailSerializer(CustomerSerializer):
    user = UserSerializer(read_only=True)


class UserDetailSerializer(UserSerializer):
    customer = CustomerSerializer(read_only=True)
