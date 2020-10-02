from django.db import models
from django.utils.translation import gettext_lazy as _

from taxonomies.models.iso_coded import *


class BasicMetaData(models.Model):
    created = models.DateTimeField(auto_now_add=True, verbose_name=_('created'))
    value = models.FloatField(max_length=200, default=0, verbose_name=_('value'))

    class Meta:
        verbose_name = _('meta data')
        verbose_name_plural = _('meta data')


class MetaDataCountry(BasicMetaData):
    taxonomy = models.OneToOneField(Country, on_delete=models.CASCADE, related_name="meta_data", verbose_name=_('taxonomy'))


class MetaDataCompanyType(BasicMetaData):
    taxonomy = models.OneToOneField(CompanyType, on_delete=models.CASCADE, related_name="meta_data", verbose_name=_('taxonomy'))


class MetaDataCurrency(BasicMetaData):
    taxonomy = models.OneToOneField(Currency, on_delete=models.CASCADE, related_name="meta_data", verbose_name=_('taxonomy'))
