from django.db import models
from django.utils.translation import gettext_lazy as _


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
