from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from api.serializers.customer import CustomerSerializer, UserSerializer
from shop.models.customer import Customer
from users.models import CustomUser


class UserViewSet(ModelViewSet):
    """
    Manage `list` and `detail` users.
    """
    serializer_class = UserSerializer
    queryset = CustomUser.objects.all()
    permission_classes = [IsAuthenticated]


class CustomerViewSet(ModelViewSet):
    """
    Manage `list` and `detail` customers.
    """
    serializer_class = CustomerSerializer
    queryset = Customer.objects.all()
    permission_classes = [IsAuthenticated]
