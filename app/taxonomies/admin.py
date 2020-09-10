from django.contrib import admin
from django.utils.translation import gettext_lazy as _

from .models import *


class BaseTaxonomyLayout(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}


class CategoryLayout(BaseTaxonomyLayout):
    model = Category


class ColorLayout(BaseTaxonomyLayout):
    model = Color


class CountryLayout(BaseTaxonomyLayout):
    model = Country


class SizeLayout(BaseTaxonomyLayout):
    model = Size


class TargetGroupLayout(BaseTaxonomyLayout):
    model = TargetGroup


admin.site.register(Category, CategoryLayout)
admin.site.register(Color, ColorLayout)
admin.site.register(Country, CountryLayout)
admin.site.register(Size, SizeLayout)
admin.site.register(TargetGroup, TargetGroupLayout)
