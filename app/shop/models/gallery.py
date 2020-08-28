from django.db import models
from django.utils.translation import gettext_lazy as _


class BaseImage(models.Model):
    # name = models.ImageField(upload_to='products/', blank=True , verbose_name=_('image'))

    @property
    def imageUrl(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url


class ProductBrandImage(BaseImage):
    image = models.ImageField(upload_to='products/brands/', blank=True , verbose_name=_('image'))


class ProductImage(BaseImage):
    image = models.ImageField(upload_to='products/', blank=True , verbose_name=_('image'))
