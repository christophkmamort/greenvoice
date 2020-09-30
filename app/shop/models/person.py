from django.db import models
from django.utils.translation import gettext_lazy as _

from .brand import Brand


class BasicPerson(models.Model):
    account_holder = models.BooleanField(blank=True, verbose_name=_('account holder'))
    firstname = models.CharField(max_length=200, blank=True, verbose_name=_('firstname'))
    lastname = models.CharField(max_length=200, blank=True, verbose_name=_('lastname'))
    id_front = models.ImageField(upload_to=create_brand_person_upload_path, blank=True, verbose_name=_('id front'), unique=True)
    id_back = models.ImageField(upload_to=create_brand_person_upload_path, blank=True, verbose_name=_('id back'), unique=True)


class BrandPerson(BasicPerson):
    brand = models.ForeignKey(Brand, blank=True, null=True, on_delete=models.CASCADE, related_name='person', verbose_name=_('brand'))
