from django.db import models
from django.utils.text import slugify
from django.utils.translation import gettext_lazy as _


class BaseTaxonomy(models.Model):
    name = models.CharField(max_length=200, null=True, verbose_name=_('name'))
    slug = models.SlugField(unique=True, null=True, verbose_name=_('slug'))
    value = models.FloatField(max_length=200, default=0, verbose_name=_('value'))
    created = models.DateTimeField(auto_now_add=True, verbose_name=_('created'))

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        try:
            self.slug = slugify(self.request.data['name'])
        except:
            pass
        return super().save(*args, **kwargs)


class Category(models.Model):
    name = models.CharField(max_length=200, null=True, verbose_name=_('name'))
    slug = models.SlugField(unique=True, null=True, verbose_name=_('slug'))
    parent = models.ForeignKey('self', blank=True, null=True, on_delete=models.CASCADE, related_name='children', verbose_name=_('parent'))
    value = models.FloatField(max_length=200, default=0, verbose_name=_('value'))
    created = models.DateTimeField(auto_now_add=True, verbose_name=_('created'))

    class Meta:
        unique_together = ('slug', 'parent',)
        verbose_name_plural = _('categories')

    def __str__(self):
        return self.name

    def __str__(self):
        full_path = [self.name]
        k = self.parent
        while k is not None:
            full_path.append(k.name)
            k = k.parent
        return ' -> '.join(full_path[::-1])


class Color(BaseTaxonomy):
    hex = models.CharField(max_length=6, null=True, verbose_name=_('hex'))


class Country(BaseTaxonomy):

    class Meta:
        verbose_name_plural = _('countries')


class Size(BaseTaxonomy):
    order = models.IntegerField(blank=True, verbose_name=_('order'))


class TargetGroup(BaseTaxonomy):

    class Meta:
        verbose_name = _('target group')
