from django.db import models
from django.utils.translation import gettext_lazy as _

from .base import BaseTaxonomy


class Color(BaseTaxonomy):
    hex = models.CharField(max_length=6, null=True, verbose_name=_('hex'))


class Size(BaseTaxonomy):
    order = models.IntegerField(blank=True, verbose_name=_('order'))
