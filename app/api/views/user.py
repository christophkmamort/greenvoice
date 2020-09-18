from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from api.serializers.user import *
from users.models.customer import Customer
from users.models import CustomUser


class UserViewSet(ModelViewSet):
    """
    Manage `list` and `detail` users.
    """
    serializer_class = UserSerializer
    queryset = CustomUser.objects.all()
    permission_classes = [IsAuthenticated]

    def get_serializer_class(self):
        """
        Return appropriate serializer class.
        """
        if self.action == 'retrieve' or self.action == 'list':
            return UserDetailSerializer
        return self.serializer_class


class CustomerViewSet(ModelViewSet):
    """
    Manage `list` and `detail` customers.
    """
    serializer_class = CustomerSerializer
    queryset = Customer.objects.all()
    permission_classes = [IsAuthenticated] # Only view and edit if self or staff (In comments also for other users name and profile pic).

    def get_serializer_class(self):
        """
        Return appropriate serializer class.
        """
        if self.action == 'retrieve' or self.action == 'list':
            return CustomerDetailSerializer
        return self.serializer_class
