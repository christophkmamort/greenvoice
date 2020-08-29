from django.db import models
from django.utils.translation import gettext_lazy as _

from .product import ProductManager


class BaseProductImage(models.Model):
    order = models.IntegerField(blank=True, verbose_name=_('order'))
    created = models.DateTimeField(auto_now_add=True, verbose_name=_('created'))

    @property
    def imageUrl(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url


class ProductBrandImage(BaseProductImage):
    image = models.ImageField(upload_to='products/brands/', blank=True, verbose_name=_('image'))
    product = models.ForeignKey(ProductManager, null=True, on_delete=models.SET_NULL, verbose_name=_('product'))


class ProductImage(BaseProductImage):
    image = models.ImageField(upload_to='products/', blank=True, verbose_name=_('image'))
    product = models.ForeignKey(ProductManager, null=True, on_delete=models.SET_NULL, verbose_name=_('product'))
