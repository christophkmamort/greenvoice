import datetime

from django.db import models
from django.utils.translation import gettext_lazy as _

from shop.models.brand import Brand
from users.models.customer import BodyMeasurements
from shop.models.product import Product, ProductManager, ProductOption
from taxonomies.models import Category, Color, Size


class AnonymousUserData(models.Model):
    body_measurements = models.OneToOneField(BodyMeasurements, null=True, on_delete=models.SET_NULL, verbose_name=_('body measurements'))
    city = models.CharField(max_length=200, blank=True, verbose_name=_('city'))
    country = models.CharField(max_length=200, blank=True, verbose_name=_('country'))
    WOMEN = 1
    MEN = 2
    GENDER_CHOICES = (
        (WOMEN, _('women')),
        (MEN, _('men')),
    )
    gender = models.PositiveSmallIntegerField(choices=GENDER_CHOICES, blank=True, verbose_name=_('gender'))
    language = models.CharField(max_length=200, blank=True, verbose_name=_('language'))
    referer = models.CharField(max_length=200, blank=True, verbose_name=_('referer'))
    state = models.CharField(max_length=200, blank=True, verbose_name=_('state'))


class BaseValueLog(models.Model):
    CLICK = 1
    WISHLIST = 2
    CART = 3
    ORDER = 4
    ACTION_CHOICES = (
        (CLICK, _('click')),
        (WISHLIST, _('wishlist')),
        (CART, _('cart')),
        (ORDER, _('order')),
    )
    action = models.PositiveSmallIntegerField(choices=ACTION_CHOICES, default=CLICK, verbose_name=_('action'))
    user = models.OneToOneField(AnonymousUserData, null=True, on_delete=models.SET_NULL, verbose_name=_('anonymous user data'))
    created = models.DateTimeField(auto_now_add=True, verbose_name=_('created'))

    def __str__(self):
        return str(self.action)

    @property
    def get_value(self):
        age = (datetime.datetime.now() - self.created.replace(tzinfo=None)).days

        if self.action == 1:
            value = .15
        elif self.action == 2 or self.action == 3:
            value = .35
        elif self.action == 4:
            value = .50

        if age > 365:
            value = value * 0
        elif age > 30:
            value = value * .15
        elif age > 7:
            value = value * .50

        return value


class BrandValueLog(BaseValueLog):
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, blank=True, null=True, verbose_name=_('brand'))

    class Meta:
        verbose_name = _('brand log')


class ProductValueLog(BaseValueLog):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, blank=True, null=True, verbose_name=_('product'))
    product_manager = models.ForeignKey(ProductManager, on_delete=models.CASCADE, blank=True, null=True, verbose_name=_('product manager'))
    product_option = models.ForeignKey(ProductOption, on_delete=models.CASCADE, blank=True, null=True, verbose_name=_('product option'))

    class Meta:
        verbose_name = _('product log')


class TaxonomyValueLog(BaseValueLog):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, blank=True, null=True, verbose_name=_('category'))
    color = models.ForeignKey(Color, on_delete=models.CASCADE, blank=True, null=True, verbose_name=_('color'))
    size = models.ForeignKey(Size, on_delete=models.CASCADE, blank=True, null=True, verbose_name=_('size'))

    class Meta:
        verbose_name = _('taxonomy log')
