from django.contrib.contenttypes.models import ContentType
from django.db import models
from django.utils.translation import gettext_lazy as _

from users.models.customer import Customer
from .product import ProductManager, ProductOption


class WishlistItem(models.Model):
    customer = models.ForeignKey(
        Customer, on_delete=models.CASCADE, null=True, related_name='wcustomer', verbose_name=_('customer'))
    product_manager = models.ForeignKey(
        ProductManager, on_delete=models.SET_NULL, null=True, verbose_name=_('product manager'))
    product_option = models.ForeignKey(
        ProductOption, on_delete=models.SET_NULL, null=True, blank=True, verbose_name=_('product option'))
    created = models.DateTimeField(
        auto_now_add=True, verbose_name=_('created'))

    def __str__(self):
        return self.product_manager.product.name

    @property
    def get_wishlist_items(self):
        wishlistitems = self.wishlistitem_set.all()
        total = wishlistitems.length
        return total
