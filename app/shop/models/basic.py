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
    company_name = models.CharField(max_length=200, blank=True, verbose_name=_('company name'), unique=True)
    company_type = models.ForeignKey(CompanyType, blank=True, null=True, on_delete=models.SET_NULL, verbose_name=_('company type'))
    email = models.EmailField(verbose_name=_('email address'), unique=True)
    phone = models.CharField(max_length=200, blank=True, verbose_name=_('phone number'), unique=True)
    line_1 = models.CharField(max_length=200, blank=True, verbose_name=_('line 1'))
    line_2 = models.CharField(max_length=200, blank=True, verbose_name=_('line 2'))
    # country = models.ForeignKey(Country, blank=True, null=True, on_delete=models.SET_NULL, verbose_name=_('country'))
    post_code = models.IntegerField(blank=True, verbose_name=_('post code'))
    tax_number = models.CharField(max_length=200, blank=True, verbose_name=_('tax number'), unique=True)


class BasicMetaData(models.Model):
    created = models.DateTimeField(auto_now_add=True, verbose_name=_('created'))
    value = models.FloatField(max_length=200, default=0, verbose_name=_('value'))

    class Meta:
        verbose_name = _('meta data')
        verbose_name_plural = _('meta data')


class BasicPerson(models.Model):
    account_holder = models.BooleanField(blank=True, verbose_name=_('account holder'))
    firstname = models.CharField(max_length=200, blank=True, verbose_name=_('firstname'))
    lastname = models.CharField(max_length=200, blank=True, verbose_name=_('lastname'))


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


class BasicTax(models.Model):
    included = models.BooleanField(blank=True, verbose_name=_('included'))


class BasicTaxZones(models.Model):
    tax = models.ForeignKey(BasicTax, blank=True, null=True, on_delete=models.CASCADE, related_name='tax_zones', verbose_name=_('tax'))
    country = models.ForeignKey(Country, blank=True, null=True, on_delete=models.SET_NULL, verbose_name=_('country'))
    rate = models.IntegerField(blank=True, verbose_name=_('rate (in %)'))
