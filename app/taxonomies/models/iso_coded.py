from django.db import models
from django.utils.translation import gettext_lazy as _

from .base import BaseTaxonomy
from shop.models.basic import BasicMetaData


"""
Country taxonomy.
"""
class Country(BaseTaxonomy):
    class Meta:
        verbose_name_plural = _('countries')


class MetaDataCountry(BasicMetaData):
    taxonomy = models.OneToOneField(Country, on_delete=models.CASCADE, related_name="meta_data", verbose_name=_('taxonomy'))


"""
Company type taxonomy.
"""
class CompanyType(models.Model): # Not `BasicMetaData` because clashes with country.
    name = models.CharField(max_length=200, null=True, verbose_name=_('name'))
    slug = models.SlugField(null=True, verbose_name=_('slug'), unique=True)
    abbreviation = models.CharField(max_length=200, null=True, verbose_name=_('abbreviation'), unique=True)
    country = models.ForeignKey(Country, blank=True, null=True, on_delete=models.SET_NULL, verbose_name=_('country'))

    """ def __str__(self):
        return str(self.name) """


class MetaDataCompanyType(BasicMetaData):
    taxonomy = models.OneToOneField(CompanyType, on_delete=models.CASCADE, related_name="meta_data", verbose_name=_('taxonomy'))


"""
Currency taxonomy.
"""
class Currency(BaseTaxonomy):
    code_iso_4217 = models.CharField(max_length=3, null=True, verbose_name=_('iso 4217 code'), unique=True)
    symbol = models.CharField(max_length=5, null=True, verbose_name=_('symbol'), unique=True)
    countries = models.ManyToManyField(Country, blank=True, related_name='currency', verbose_name=_('countries'))

    class Meta:
        verbose_name_plural = _('currencies')


class MetaDataCurrency(BasicMetaData):
    taxonomy = models.OneToOneField(Currency, on_delete=models.CASCADE, related_name="meta_data", verbose_name=_('taxonomy'))
