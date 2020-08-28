from url_filter.integrations.drf import DjangoFilterBackend

from rest_framework.decorators import action, api_view
from rest_framework.filters import OrderingFilter, SearchFilter
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


# brand


# category


# value log


"""class DynamicSearchFilter(SearchFilter):
    def get_search_fields(self, view, request):
        return request.GET.getlist('search') # .GET.getlist('search_fields', [])"""


# product


# custom user, customer


# order, order detail
