import os

from django.db import models
from django.utils.translation import gettext_lazy as _

from .product import ProductManager


def create_product_brand_image_path(self, filename):
    return os.path.join('brands', self.product_manager.product.brand.name, 'products', self.product_manager.product.name, 'brand', filename)


def create_product_image_path(self, filename):
    return os.path.join('brands', self.product_manager.product.brand.name, 'products', self.product_manager.product.name, filename)


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
    image = models.ImageField(upload_to=create_product_brand_image_path, blank=True, verbose_name=_('image'))
    product_manager = models.ForeignKey(ProductManager, null=True, on_delete=models.SET_NULL, verbose_name=_('product'))


class ProductImage(BaseProductImage):
    image = models.ImageField(upload_to=create_product_image_path, blank=True, verbose_name=_('image'))
    product_manager = models.ForeignKey(ProductManager, null=True, on_delete=models.SET_NULL, verbose_name=_('product'))
