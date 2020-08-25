import datetime

from django.db import models
from django.utils.translation import gettext_lazy as _

from .brand import Brand
from .product import Product
from .taxonomies import Category


class ValueLog(models.Model):
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, blank=True, null=True, verbose_name=_('brand'))
    product = models.ForeignKey(Product, on_delete=models.CASCADE, blank=True, null=True, verbose_name=_('product'))
    category = models.ForeignKey(Category, on_delete=models.CASCADE, blank=True, null=True, verbose_name=_('category'))
    CLICK = 1
    WISHLIST = 2
    CART = 3
    ORDER = 4
    ACTION_CHOICES = (
        (CLICK, _('click')),
        (WISHLIST, _('wishlist')),
        (CART, _('cart')),
        (ORDER, _('order')),
    )
    action = models.PositiveSmallIntegerField(choices=ACTION_CHOICES, default=CLICK, verbose_name=_('action'))
    created = models.DateTimeField(auto_now_add=True, verbose_name=_('created'))

    def __str__(self):
        return str(self.action)

    @property
    def get_value(self):
        age = (datetime.datetime.now() - self.created.replace(tzinfo=None)).days

        if self.action == 1:
            value = .15
        elif self.action == 2 or self.action == 3:
            value = .35
        elif self.action == 4:
            value = .50

        if age > 365:
            value = value * 0
        elif age > 30:
            value = value * .15
        elif age > 7:
            value = value * .50

        return value
