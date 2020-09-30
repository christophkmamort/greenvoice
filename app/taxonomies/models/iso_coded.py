from django.db import models
from django.utils.translation import gettext_lazy as _

from .base import BaseTaxonomy


class Country(BaseTaxonomy):

    class Meta:
        verbose_name_plural = _('countries')


class CompanyType(models.Model):
    name = models.CharField(max_length=200, null=True, verbose_name=_('name'))
    country = models.ForeignKey(Country, blank=True, null=True, on_delete=models.SET_NULL, verbose_name=_('country'))


class Currency(models.Model):
    name = models.CharField(max_length=200, null=True, verbose_name=_('name'), unique=True)
    code_iso_4217 = models.CharField(max_length=3, null=True, verbose_name=_('iso 4217 code'), unique=True)
    symbol = models.CharField(max_length=5, null=True, verbose_name=_('symbol'), unique=True)
