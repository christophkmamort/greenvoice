from django.db import models
from django.utils.translation import gettext_lazy as _

from .brand import Brand
from .taxonomies import Category


class Product(models.Model):
    brand = models.ForeignKey(Brand, blank=True, on_delete=models.CASCADE, verbose_name=_('brand'))
    name = models.CharField(max_length=200, blank=True, verbose_name=_('name'))
    UNISEX = 1
    WOMEN = 2
    MEN = 3
    GENDER_CHOICES = (
        (UNISEX, _('unisex')),
        (WOMEN, _('women')),
        (MEN, _('men')),
    )
    gender = models.PositiveSmallIntegerField(choices=GENDER_CHOICES, default=UNISEX, verbose_name=_('gender'))
    category = models.ManyToManyField(Category, blank=True, verbose_name=_('category'))
    query = models.CharField(max_length=200, blank=True, verbose_name=_('queryset'))
    price = models.FloatField(blank=True, verbose_name=_('price'))
    image = models.ImageField(upload_to='products/', blank=True , verbose_name=_('image'))
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
    value = models.FloatField(max_length=200, default=0, verbose_name=_('value'))
    created = models.DateTimeField(auto_now_add=True, verbose_name=_('created'))

    class Meta:
        ordering = ['created']

    def __str__(self):
        return self.name

    @property
    def imageUrl(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url


    """def save(self, *args, **kwargs):
        options = {'title': self.title} if self.title else {}
        super(Product, self).save(*args, **kwargs)"""
