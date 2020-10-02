from django.db import models
from django.utils.translation import gettext_lazy as _

from .base import BaseTaxonomy


"""
Country taxonomy.
"""
class Country(BaseTaxonomy):
    class Meta:
        verbose_name_plural = _('countries')


"""
Company type taxonomy.
"""
class CompanyType(models.Model):
    name = models.CharField(max_length=200, null=True, verbose_name=_('name'))
    slug = models.SlugField(null=True, verbose_name=_('slug'), unique=True)
    abbreviation = models.CharField(max_length=200, null=True, verbose_name=_('abbreviation'), unique=True)
    country = models.ForeignKey(Country, blank=True, null=True, on_delete=models.SET_NULL, verbose_name=_('country'))

    def __str__(self):
        return str(self.name)

    def save(self, *args, **kwargs):
        try:
            self.slug = slugify(self.request.data['name'])
        except:
            pass
        return super().save(*args, **kwargs)


"""
Currency taxonomy.
"""
class Currency(BaseTaxonomy):
    code_iso_4217 = models.CharField(max_length=3, null=True, verbose_name=_('iso 4217 code'), unique=True)
    symbol = models.CharField(max_length=5, null=True, verbose_name=_('symbol'), unique=True)
    countries = models.ManyToManyField(Country, blank=True, related_name='currency', verbose_name=_('countries'))

    class Meta:
        verbose_name_plural = _('currencies')
