from io import BytesIO
from PIL import Image
import os

from django.core.files.uploadedfile import InMemoryUploadedFile
from django.db import models
from django.utils.translation import gettext_lazy as _

from .product import ProductManager


def create_product_brand_image_path(self, filename):
    return os.path.join('brands', self.product_manager.product.brand.name.lower().replace(' ', '-'), 'products', self.product_manager.product.name.lower().replace(' ', '-'), self.product_manager.color.slug, 'brand', filename.lower().replace(' ', '-'))


def create_product_image_path(self, filename):
    return os.path.join('brands', self.product_manager.product.brand.name.lower().replace(' ', '-'), 'products', self.product_manager.product.name.lower().replace(' ', '-'), self.product_manager.color.slug,  filename.lower().replace(' ', '-'))


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
    product_manager = models.ForeignKey(ProductManager, null=True, on_delete=models.SET_NULL, related_name='brand_image', verbose_name=_('product'))

    def save(self, *args, **kwargs):
        image = Image.open(self.image)
        width = 640
        if image.size[0] > width:
            hpercent = (width/float(image.size[0]))
            height = int(image.size[1]*float(hpercent))
            size = (width, height)
            image = image.resize(size, resample=0, box=None)
            thumb_io = BytesIO()
            image.save(thumb_io, format='JPEG', optimize=True, quality=50)
            inmemory_uploaded_file = InMemoryUploadedFile(thumb_io, None, self.image.name.split('.')[0] + '.jpg', 'image/jpeg', thumb_io.tell(), None)
            self.image = inmemory_uploaded_file
        super(ProductBrandImage, self).save(*args, **kwargs)


class ProductImage(BaseProductImage):
    image = models.ImageField(upload_to=create_product_image_path, blank=True, verbose_name=_('image'))
    product_manager = models.ForeignKey(ProductManager, null=True, on_delete=models.SET_NULL, related_name='image', verbose_name=_('product'))

    def save(self, *args, **kwargs):
        image = Image.open(self.image)
        width = 640
        if image.size[0] > width:
            hpercent = (width/float(image.size[0]))
            height = int(image.size[1]*float(hpercent))
            size = (width, height)
            image = image.resize(size, resample=0, box=None)
            thumb_io = BytesIO()
            image.save(thumb_io, format='JPEG', optimize=True, quality=50)
            inmemory_uploaded_file = InMemoryUploadedFile(thumb_io, None, self.image.name.split('.')[0] + '.jpg', 'image/jpeg', thumb_io.tell(), None)
            self.image = inmemory_uploaded_file
        super(ProductImage, self).save(*args, **kwargs)
