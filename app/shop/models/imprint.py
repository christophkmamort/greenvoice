from django.db import models
from django.utils.translation import gettext_lazy as _

from taxonomies.models.iso_coded import Country, CompanyType


class BasicImprint(models.Model):
    company_name = models.CharField(max_length=200, blank=True, verbose_name=_('company name'), unique=True)
    company_type = models.ForeignKey(CompanyType, blank=True, null=True, on_delete=models.SET_NULL, verbose_name=_('company type'))
    email = models.EmailField(verbose_name=_('email address'), unique=True)
    phone = models.CharField(max_length=200, blank=True, verbose_name=_('phone number'), unique=True)
    line_1 = models.CharField(max_length=200, blank=True, verbose_name=_('line 1'))
    line_2 = models.CharField(max_length=200, blank=True, verbose_name=_('line 2'))
    country = models.ForeignKey(Country, blank=True, null=True, on_delete=models.SET_NULL, verbose_name=_('country'))
    post_code = models.IntegerField(blank=True, verbose_name=_('post code'))
    tax_number = models.CharField(max_length=200, blank=True, verbose_name=_('tax number'), unique=True)
