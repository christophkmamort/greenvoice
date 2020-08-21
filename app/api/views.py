from rest_framework import generics
from rest_framework.decorators import action, api_view
from rest_framework.filters import OrderingFilter
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser, IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet

from .permissions import IsCustomerOrStaff
from .serializers import OrderSerializer, OrderItemSerializer, \
                        ProductSerializer, UserSerializer, CustomerSerializer
from shop.models.customer import Customer
from shop.models.product import Product
from shop.models.order import Order, OrderItem
from users.models import CustomUser


@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'orders': reverse('order-list', request=request, format=format),
        'users': reverse('user-list', request=request, format=format),
        'customer': reverse('customer-list', request=request, format=format),
        'products': reverse('product-list', request=request, format=format)
    })


class ProductViewSet(ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.
    """
    queryset = Product.objects.all()
    filter_backends = [OrderingFilter]
    ordering_fields = ['created',]
    ordering = ['created']
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save()


class UserViewSet(ReadOnlyModelViewSet):
    """
    This viewset automatically provides `list` and `detail` actions.
    """
    serializer_class = UserSerializer
    queryset = CustomUser.objects.all()
    permission_classes = [IsAuthenticated, IsAdminUser]


class CustomerViewSet(ModelViewSet):
    """
    This viewset automatically provides `list` and `detail` actions.
    """
    serializer_class = CustomerSerializer
    queryset = Customer.objects.all()
    permission_classes = [IsAuthenticated] # , IsAdminUser


class OrderViewSet(ModelViewSet): # ModelViewSet
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.
    """
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated] # , IsCustomerOrStaff

    def get_queryset(self):
        return Order.objects.filter(customer=self.request.user.customer)

    def perform_create(self, serializer):
        serializer.save(customer=self.request.user.customer)


class OrderItemViewSet(ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.
    """
    serializer_class = OrderItemSerializer
    permission_classes = [IsAuthenticated] # , IsCustomerOrStaff

    def get_queryset(self):
        return OrderItem.objects.filter(order=4)

    def perform_create(self, serializer):
        serializer.save() # order = ..
