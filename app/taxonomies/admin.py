from django.contrib import admin
from django.utils.translation import gettext_lazy as _

from .models import *


class BaseTaxonomyLayout(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}


class CategoryLayout(BaseTaxonomyLayout):
    model = Category
    verbose_name = _('category')
    verbose_name_plural = _('categories')


class ColorLayout(BaseTaxonomyLayout):
    model = Color


class CountryLayout(BaseTaxonomyLayout):
    model = Color


class SizeLayout(BaseTaxonomyLayout):
    model = Color


class TargetGroupLayout(BaseTaxonomyLayout):
    model = Color


admin.site.register(Category, CategoryLayout)
admin.site.register(Color)
admin.site.register(Country)
admin.site.register(Size)
admin.site.register(TargetGroup)
