from django.db import models
from django.utils.translation import gettext_lazy as _


class Brand(models.Model):
    name = models.CharField(max_length=200, verbose_name=_('name'), blank=True)
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
    status = models.PositiveSmallIntegerField(choices=STATUS_CHOICES, default=DRAFT, verbose_name=_('status'))
    created = models.DateTimeField(auto_now_add=True, verbose_name=_('created'))

    class Meta:
        ordering = ['created']

    def __str__(self):
        return self.name
