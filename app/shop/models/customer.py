from django.conf import settings
from django.db import models
from django.utils.translation import gettext_lazy as _


class Customer(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name=_('user'))
    name = models.CharField(max_length=200, blank=True, verbose_name=_('name'))
    created = models.DateTimeField(auto_now_add=True, verbose_name=_('created'))

    class Meta:
        ordering = ['created']

    def __str__(self):
        return self.name
