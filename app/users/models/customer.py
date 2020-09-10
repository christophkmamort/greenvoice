from django.conf import settings
from django.db import models
from django.utils.translation import gettext_lazy as _


class Address(models.Model):
    line_1 = models.CharField(max_length=200, blank=True, verbose_name=_('line 1'))
    line_2 = models.CharField(max_length=200, blank=True, verbose_name=_('line 2'))
    city = models.CharField(max_length=200, blank=True, verbose_name=_('city'))
    zip = models.CharField(max_length=200, blank=True, verbose_name=_('postal code'))
    country = models.CharField(max_length=200, blank=True, verbose_name=_('country'))


class BodyMeasurements(models.Model):
    age = models.IntegerField(blank=True, verbose_name=_('age'))
    chest = models.IntegerField(blank=True, verbose_name=_('chest'))
    hip = models.IntegerField(blank=True, verbose_name=_('hip'))
    inseam = models.IntegerField(blank=True, verbose_name=_('inseam'))
    size = models.IntegerField(blank=True, verbose_name=_('size'))
    sleeve_length = models.IntegerField(blank=True, verbose_name=_('sleeve length'))
    thigh = models.CharField(max_length=200, blank=True, verbose_name=_('thigh'))
    upper_arm = models.IntegerField(blank=True, verbose_name=_('upper arm'))
    waist = models.IntegerField(blank=True, verbose_name=_('waist'))


class Customer(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, null=True, on_delete=models.CASCADE, verbose_name=_('user'))

    WOMEN = 1
    MEN = 2
    GENDER_CHOICES = (
        (WOMEN, _('women')),
        (MEN, _('men')),
    )
    gender = models.PositiveSmallIntegerField(choices=GENDER_CHOICES, null=True, blank=True, verbose_name=_('gender'))
    name = models.CharField(max_length=200, blank=True, verbose_name=_('name'))
    address = models.OneToOneField(Address, null=True, on_delete=models.SET_NULL, verbose_name=_('address'))

    body_measurements = models.OneToOneField(BodyMeasurements, null=True, on_delete=models.SET_NULL, verbose_name=_('body measurements'))

    created = models.DateTimeField(auto_now_add=True, verbose_name=_('created'))

    class Meta:
        ordering = ['created']

    def __str__(self):
        return self.name
