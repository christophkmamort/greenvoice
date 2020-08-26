from url_filter.integrations.drf import DjangoFilterBackend

from rest_framework.decorators import action, api_view
from rest_framework.filters import OrderingFilter
from rest_framework.permissions import IsAuthenticated, IsAdminUser, \
                                    IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet

from .permissions import IsCustomerOrStaff
from .serializers import *
from shop.models.taxonomies import Category
from shop.models.brand import Brand
from shop.models.customer import Customer
from shop.models.product import Product
from shop.models.log import ValueLog
from shop.models.order import Order, OrderItem
from users.models import CustomUser


@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'category': reverse('category-list', request=request, format=format),
        'orders': reverse('order-list', request=request, format=format),
        'users': reverse('user-list', request=request, format=format),
        'customer': reverse('customer-list', request=request, format=format),
        'products': reverse('product-list', request=request, format=format),
        'value-log': reverse('value-log-list', request=request, format=format),
    })


class BrandViewSet(ModelViewSet):
    """
    Manage `list`, `create`, `retrieve`, `update` and `destroy` brands.
    """
    queryset = Brand.objects.all()
    filter_backends = [OrderingFilter]
    ordering_fields = ['created', 'value',]
    ordering = ['-value']
    serializer_class = BrandSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    # def get_queryset(self):
    """
    Filter brands to have specific `products`.
    """
    # queryset = Brand.objects.all()

    """product = self.request.query_params.get('product', None)
    if product is not None:
        queryset = queryset.filter(product=product).distinct()"""

    # return queryset

    def perform_create(self, serializer):
        serializer.save()


class CategoryViewSet(ModelViewSet):
    """
    Manage `list`, `create`, `retrieve`, `update` and `destroy` brands.
    """
    filter_backends = [OrderingFilter]
    ordering_fields = ['created', 'value',]
    ordering = ['-value']
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        """
        Only display categories that are assosiated with a `product`.
        """
        queryset = Category.objects.filter(product__isnull=False).distinct()
        return queryset

    def perform_create(self, serializer):
        serializer.save(slug=self.request.data['name'].lower())


class ValueLogViewSet(ModelViewSet):
    """
    Manage `list`, `create`, `retrieve`, `update` and `destroy` product log.
    """
    queryset = ValueLog.objects.all()
    filter_backends = [OrderingFilter]
    ordering_fields = ['created',]
    ordering = ['-created']
    serializer_class = ValueLogSerializer

    def perform_create(self, serializer):
        serializer.save()


class ProductViewSet(ModelViewSet):
    """
    Manage `list`, `create`, `retrieve`, `update` and `destroy` products.
    """
    queryset = Product.objects.all()
    filter_backends = [OrderingFilter, DjangoFilterBackend]
    filter_fields = ['brand', 'category', 'price']
    ordering_fields = ['created', 'price', 'value']
    ordering = ['-value']
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    #def get_queryset(self):
    """
    Filter products to have specific `brand`.
    """
    """queryset = Product.objects.all()

    brands = self.request.query_params.get('brands', None)
    if brands is not None:
        queryset = queryset.filter(brand__in=brands)

    category_name = self.request.query_params.get('category', None)
    if category_name:
        category = Category.objects.get(name=category_name)
        if category is not None:
            queryset = queryset.filter(category=category)

    price_max = self.request.query_params.get('price_max', None)
    if price_max is not None:
        queryset = queryset.filter(price__lte=price_max)

    price_min = self.request.query_params.get('price_min', None)
    if price_min is not None:
        queryset = queryset.filter(price__gte=price_min)

    return queryset"""

    def perform_create(self, serializer):
        serializer.save()


class UserViewSet(ReadOnlyModelViewSet):
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
    permission_classes = [IsAuthenticated] # , IsAdminUser


class OrderViewSet(ModelViewSet): # ModelViewSet
    """
    Manage `list`, `create`, `retrieve`, `update` and `destroy` orders.
    """
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated] # , IsCustomerOrStaff

    def get_queryset(self):
        return Order.objects.filter(customer=self.request.user.customer)

    def perform_create(self, serializer):
        serializer.save(customer=self.request.user.customer)

    def perform_update(self, serializer):
        serializer.save(customer=self.request.user.customer)

    """def perform_destroy(self, instance):"""


class OrderItemViewSet(ModelViewSet):
    """
    Manage `list`, `create`, `retrieve`, `update` and `destroy` order-items.
    """
    serializer_class = OrderItemSerializer
    permission_classes = [IsAuthenticated] # , IsCustomerOrStaff

    def get_serializer_class(self):
        """Return appropriate serializer class"""
        if self.action == 'retrieve':
            return OrderItemDetailSerializer

        return self.serializer_class

    def get_queryset(self):
        return OrderItem.objects.filter(customer=self.request.user.customer)

    def perform_create(self, serializer):
        serializer.save(customer=self.request.user.customer)

    def perform_update(self, serializer):
        serializer.save(customer=self.request.user.customer)
