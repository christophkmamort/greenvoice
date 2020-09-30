from django.db import models
from django.utils.translation import gettext_lazy as _

from taxonomies.models.iso_coded import Country, Currency


class BasicBanking(models.Model):
    iban = models.CharField(max_length=20, blank=True, verbose_name=_('iban'))
    bic = models.CharField(max_length=20, blank=True, verbose_name=_('bic'))
    currency = models.ForeignKey(Currency, blank=True, null=True, on_delete=models.SET_NULL, verbose_name=_('currency'))
    country = models.ForeignKey(Country, blank=True, null=True, on_delete=models.SET_NULL, verbose_name=_('country'))
