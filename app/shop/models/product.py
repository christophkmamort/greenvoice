from django.db import models
from django.utils.translation import gettext_lazy as _

from .brand import Brand
from .taxonomies import Category, Color, Size


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
    # Add transparency manager here!!
    query = models.CharField(max_length=200, blank=True, verbose_name=_('queryset'))
    value = models.FloatField(max_length=200, default=0, verbose_name=_('value'))
    created = models.DateTimeField(auto_now_add=True, verbose_name=_('created'))

    def __str__(self):
        return self.name


class ProductManager(models.Model):
    product = models.ForeignKey(Product, null=True, on_delete=models.CASCADE, verbose_name=_('product'))
    color = models.ForeignKey(Color, blank=True, null=True, on_delete=models.SET_NULL, verbose_name=_('color'))
    # Add transparency manager here!!
    value = models.FloatField(max_length=200, default=0, verbose_name=_('value'))
    created = models.DateTimeField(auto_now_add=True, verbose_name=_('created'))

    def __str__(self):
        return self.product.name + self.color


class ProductOption(models.Model):
    product_manager = models.ForeignKey(ProductManager, null=True, on_delete=models.CASCADE, verbose_name=_('product'))
    product_number =  models.CharField(max_length=200, blank=True, verbose_name=_('product number'))
    size = models.ForeignKey(Size, blank=True, null=True, on_delete=models.SET_NULL, verbose_name=_('size'))
    stock = models.IntegerField(blank=True, default=0, verbose_name=_('stock'))
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
        return self.product_manager.product.name + self.product_manager.color + self.size
