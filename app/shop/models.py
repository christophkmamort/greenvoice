from django.db import models
from django.utils.translation import gettext_lazy as _


class Product(models.Model):
    title = models.CharField(max_length=200, verbose_name=_('title'))
    price = models.FloatField(verbose_name=_('price'))
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
    status = models.PositiveSmallIntegerField(choices=STATUS_CHOICES, default=DRAFT, verbose_name=_('status'))
    created = models.DateTimeField(auto_now_add=True, verbose_name=_('created'))
    owner = models.ForeignKey('auth.User', related_name='products', on_delete=models.CASCADE)

    class Meta:
        ordering = ['created']

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        options = {'title': self.title} if self.title else {}
        super(Product, self).save(*args, **kwargs)
