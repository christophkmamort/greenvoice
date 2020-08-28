from django.db import models
from django.utils.translation import gettext_lazy as _

from .brand import Brand
from .gallery import ProductBrandImage, ProductImage
from .taxonomies import Category, Color, Size


class ProductOption(models.Model):
    product_number =  models.CharField(max_length=200, blank=True, verbose_name=_('product number'))
    color = models.ForeignKey(Color, blank=True, null=True, on_delete=models.SET_NULL, verbose_name=_('color'))
    size = models.ForeignKey(Size, blank=True, null=True, on_delete=models.SET_NULL, verbose_name=_('size'))
    # manage_stock = models.BooleanField(default=False, verbose_name=_('manage stock'))
    stock = models.IntegerField(blank=True, default=0, verbose_name=_('stock'))
    gallery = models.ManyToManyField(ProductImage, blank=True, verbose_name=_('gallery'))
    brand_gallery = models.ManyToManyField(ProductBrandImage, blank=True, verbose_name=_('brand gallery'))
    gross = models.FloatField(blank=True, verbose_name=_('price gross'))
    tax = models.FloatField(blank=True, verbose_name=_('price tax'))
    net = models.FloatField(blank=True, verbose_name=_('price net'))
    # Add transparency manager here!!
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

    def __str__(self):
        return self.color + self.size


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
    options = models.ManyToManyField(ProductOption, blank=True, verbose_name=_('options'))
    # price = models.FloatField(blank=True, verbose_name=_('price'))
    # image = models.ImageField(upload_to='products/', blank=True , verbose_name=_('image'))
    """DRAFT = 1
    PUBLISHED = 2
    PAUSED = 3
    RETIRED = 4
    STATUS_CHOICES = (
        (DRAFT, _('draft')),
        (PUBLISHED, _('published')),
        (PAUSED, _('paused')),
        (RETIRED, _('retired')),
    )
    status = models.PositiveSmallIntegerField(choices=STATUS_CHOICES, default=DRAFT, verbose_name=_('status'))"""
    # value = models.FloatField(max_length=200, default=0, verbose_name=_('value'))
    created = models.DateTimeField(auto_now_add=True, verbose_name=_('created'))

    def __str__(self):
        return self.name

    """@property
    def imageUrl(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url"""
