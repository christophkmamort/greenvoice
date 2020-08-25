from django.db import models
from django.utils.translation import gettext_lazy as _


class Brand(models.Model):
    name = models.CharField(max_length=200, verbose_name=_('name'), blank=True)
    logo = models.ImageField(upload_to='brands/', blank=True, verbose_name=_('logo'))
    DRAFT = 1
    PUBLISHED = 2
    PAUSED = 3
    RETIRED = 4
    STATUS_CHOICES = (
        (DRAFT, _('draft')),
        (PUBLISHED, _('published')),
        (PAUSED, _('paused')),
        (RETIRED, _('retired')),
    )
    value = models.FloatField(max_length=200, default=0, verbose_name=_('value'))
    status = models.PositiveSmallIntegerField(choices=STATUS_CHOICES, default=DRAFT, verbose_name=_('status'))
    created = models.DateTimeField(auto_now_add=True, verbose_name=_('created'))

    class Meta:
        ordering = ['created']

    def __str__(self):
        return self.name
