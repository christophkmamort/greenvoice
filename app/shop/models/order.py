from django.contrib.contenttypes.models import ContentType
from django.db import models
from django.utils.translation import gettext_lazy as _

from users.models.customer import Customer
from .product import ProductOption


class Order(models.Model):
    customer = models.ForeignKey(
        Customer, on_delete=models.CASCADE, null=True, related_name='customer', verbose_name=_('customer'))
    DRAFT = 1
    ORDERED = 2
    COMPLETED = 3
    STATUS_CHOICES = (
        (DRAFT, _('draft')),
        (ORDERED, _('ordered')),
        (COMPLETED, _('completed')),
    )
    status = models.PositiveSmallIntegerField(
        choices=STATUS_CHOICES, default=DRAFT, verbose_name=_('status'))

    @property
    def get_cart_items(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.quantity for item in orderitems])
        return total

    @property
    def get_cart_total(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.get_total for item in orderitems])
        return total


class OrderItem(models.Model):
    customer = models.ForeignKey(
        Customer, on_delete=models.CASCADE, null=True, verbose_name=_('customer'))
    order = models.ForeignKey(Order, on_delete=models.CASCADE,
                              null=True, related_name='order_items', verbose_name=_('order'))
    product_option = models.ForeignKey(
        ProductOption, on_delete=models.SET_NULL, null=True, verbose_name=_('product'))
    quantity = models.IntegerField(
        default=0, null=True, verbose_name=_('quantity'))

    def __str__(self):
        return self.product.name

    @property
    def get_total(self):
        total = self.product.price * self.quantity
        return total
        return content_type
