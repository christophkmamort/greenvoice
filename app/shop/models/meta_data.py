from django.db import models
from django.utils.translation import gettext_lazy as _

from .basic import BasicMetaData
from taxonomies.models.iso_coded import *


class MetaDataCountry(BasicMetaData):
    taxonomy = models.OneToOneField(Country, on_delete=models.CASCADE, related_name="meta_data", verbose_name=_('taxonomy'))


class MetaDataCompanyType(BasicMetaData):
    taxonomy = models.OneToOneField(CompanyType, on_delete=models.CASCADE, related_name="meta_data", verbose_name=_('taxonomy'))


class MetaDataCurrency(BasicMetaData):
    taxonomy = models.OneToOneField(Currency, on_delete=models.CASCADE, related_name="meta_data", verbose_name=_('taxonomy'))
