from django.db import models
from django.utils.translation import gettext_lazy as _

from .status import BasicStatus


class BrandSettings(models.Model):
    backorders = models.BooleanField(default=False, blank=True, verbose_name=_('backorders'))
    free_shipping_from = models.FloatField(blank=True, null=True, verbose_name=_('free shipping from'))
    return_policy_period = models.IntegerField(blank=True, null=True, verbose_name=_('return policy period')) # default=30,
    return_shipping_costs = models.BooleanField(default=True, blank=True, verbose_name=_('return shipping costs'))
    # stores = models.

    # TODO: Add stores selection in which brand want's to sell it's products to.


class BrandSaleSettings(models.Model):
    brand_settings = models.ForeignKey(BrandSettings, on_delete=models.CASCADE, related_name='sale', verbose_name=_('brand settings'))
    amount = models.FloatField(blank=True, null=True, verbose_name=_('amount (in %)'))
    from_datetime = models.DateTimeField(verbose_name=_('status from'))
    until_datetime = models.DateTimeField(verbose_name=_('status until'))


class BrandSettingsStatus(BasicStatus):
    brand_settings = models.ForeignKey(BrandSettings, null=True, on_delete=models.CASCADE, related_name='status', verbose_name=_('brand settings'))
