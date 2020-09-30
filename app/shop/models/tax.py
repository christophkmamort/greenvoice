from django.db import models
from django.utils.translation import gettext_lazy as _

from taxonomies.models.iso_coded import Country


class BasicTax(models.Model):
    included = models.BooleanField(blank=True, verbose_name=_('included'))


class TaxZones(models.Model):
    tax = models.ForeignKey(BasicTax, blank=True, null=True, on_delete=models.CASCADE, related_name='tax_zones', verbose_name=_('tax'))
    country = models.ForeignKey(Country, blank=True, null=True, on_delete=models.SET_NULL, verbose_name=_('country'))
    rate = models.IntegerField(blank=True, verbose_name=_('rate (in %)'))
