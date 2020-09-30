from django.db import models
from django.utils.translation import gettext_lazy as _


class BrandSettings(models.Model):
    backorders = models.BooleanField(default=False, blank=True, verbose_name=_('backorders'))
    free_shipping_from ... 
