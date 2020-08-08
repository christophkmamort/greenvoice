from django.contrib import admin
from django.utils.translation import gettext_lazy as _

from shop.models.order import Order, OrderItem


admin.site.register(Order)
admin.site.register(OrderItem)
