from django.db import models
from django.utils.translation import gettext_lazy as _


class BasicApi(models.Model):
    home_url = models.URLField(max_length=200, blank=True, verbose_name=_('home url'))
    key = models.CharField(max_length=200, blank=True, verbose_name=_('key'))
    secret = models.CharField(max_length=200, blank=True, verbose_name=_('secret'))
