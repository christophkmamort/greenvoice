from django.db import models
from django.utils.translation import gettext_lazy as _

from taxonomies.models.iso_coded import Country, CompanyType, Currency


class BasicApi(models.Model):
    home_url = models.URLField(max_length=200, blank=True, verbose_name=_('home url'))
    key = models.CharField(max_length=200, blank=True, verbose_name=_('key'))
    secret = models.CharField(max_length=200, blank=True, verbose_name=_('secret'))


class BasicBanking(models.Model):
    iban = models.CharField(max_length=20, blank=True, verbose_name=_('iban'))
    bic = models.CharField(max_length=20, blank=True, verbose_name=_('bic'))
    currency = models.ForeignKey(Currency, blank=True, null=True, on_delete=models.SET_NULL, verbose_name=_('currency'))
    country = models.ForeignKey(Country, blank=True, null=True, on_delete=models.SET_NULL, verbose_name=_('country'))


class BasicImprint(models.Model):
    company_name = models.CharField(max_length=200, verbose_name=_('company name'))
    company_type = models.ForeignKey(CompanyType, on_delete=models.PROTECT, verbose_name=_('company type'))
    email = models.EmailField(verbose_name=_('email address'), unique=True)
    phone = models.CharField(max_length=200, verbose_name=_('phone number'), unique=True)
    line_1 = models.CharField(max_length=200, verbose_name=_('line 1'))
    line_2 = models.CharField(blank=True, max_length=200, verbose_name=_('line 2'))
    post_code = models.IntegerField(verbose_name=_('post code'))
    city = models.CharField(max_length=200, verbose_name=_('city'))
    country = models.ForeignKey(Country, on_delete=models.PROTECT, verbose_name=_('country'))
    tax_number = models.CharField(max_length=200, verbose_name=_('tax number'), unique=True)


class BasicTax(models.Model):
    included = models.BooleanField(blank=True, verbose_name=_('included'))


class BasicTaxZones(models.Model):
    tax = models.ForeignKey(BasicTax, blank=True, null=True, on_delete=models.CASCADE, related_name='tax_zones', verbose_name=_('tax'))
    country = models.ForeignKey(Country, blank=True, null=True, on_delete=models.SET_NULL, verbose_name=_('country'))
    rate = models.IntegerField(blank=True, verbose_name=_('rate (in %)'))
