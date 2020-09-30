from django.db import models
from django.utils.translation import gettext_lazy as _

from product import *
from .settings import BrandSettings
from .product import *


class BasicStatus(models.Model):
    created = models.DateTimeField(auto_now_add=True, verbose_name=_('created'))
    DRAFT = 1
    LIVE = 2
    PAUSED = 3
    RETIRED = 4
    STATUS_CHOICES = (
        (DRAFT, _('draft')),
        (LIVE, _('live')),
        (PAUSED, _('paused')),
        (RETIRED, _('retired')),
    )
    from_datetime = models.DateTimeField(verbose_name=_('status from'))
    until_datetime = models.DateTimeField(verbose_name=_('status until'))
    status = models.PositiveSmallIntegerField(choices=STATUS_CHOICES, default=DRAFT, verbose_name=_('status'))

    def __str__(self):
        return self.status


class BrandSettingsStatus(BasicStatus):
    brand_settings = models.ForeignKey(BrandSettings, null=True, on_delete=models.CASCADE, related_name='status', verbose_name=_('brand settings'))


class ProductStatus(BasicStatus):
    product = models.ForeignKey(Product, null=True, on_delete=models.CASCADE, related_name='status', verbose_name=_('product'))


class ProductManagerStatus(BasicStatus):
    product_manager = models.ForeignKey(ProductManager, null=True, on_delete=models.CASCADE, related_name='status', verbose_name=_('product manager'))


class ProductOptionStatus(BasicStatus):
    product_option = models.ForeignKey(ProductOption, null=True, on_delete=models.CASCADE, related_name='status', verbose_name=_('product option'))
