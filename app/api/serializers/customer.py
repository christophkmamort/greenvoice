from rest_framework.serializers import ModelSerializer

from shop.models.customer import Customer
from users.models import CustomUser


class UserSerializer(ModelSerializer):

    class Meta:
        model = CustomUser
        fields = ['url', 'last_login', 'is_superuser', 'email', 'is_staff', 'is_active', 'date_joined', 'user_permissions',]


class CustomerSerializer(ModelSerializer):

    class Meta:
        model = Customer
        fields = '__all__'
