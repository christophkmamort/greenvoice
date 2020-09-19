from django.contrib import admin
from django.utils.translation import gettext_lazy as _

from shop.models.order import Order, OrderItem


class SaveRequestCustomer(admin.ModelAdmin):
    def save_model(self, request, obj, form, change):
        obj.customer = request.user.customer
        super().save_model(request, obj, form, change)


admin.site.register(Order, SaveRequestCustomer)
admin.site.register(OrderItem, SaveRequestCustomer)
