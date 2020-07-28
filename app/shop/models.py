from django.db import models
from django.utils.translation import gettext_lazy as _

class Product(models.Model):
    title = models.CharField(max_length=200, verbose_name=_('title'))
    price = models.FloatField(null=True, verbose_name=_('price'))
    image = models.ImageField(verbose_name=_('image'))
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
    status = models.PositiveSmallIntegerField(choices=STATUS_CHOICES, default=DRAFT, null=True, verbose_name=_('status'))

    def __str__(self):
        return self.title
