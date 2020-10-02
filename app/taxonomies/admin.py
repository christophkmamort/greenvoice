from django.contrib import admin
from django.utils.translation import gettext_lazy as _

from .models import *
from shop.models.meta_data import MetaDataCountry


"""
Basic layout logic for all taxonomies.
"""
class BasicTaxonomyLayout(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}


"""
Country taxonomy layout.
"""
class MetaDataCountryLayout(admin.TabularInline):
    model = MetaDataCountry


class TaxonomyCountryLayout(BasicTaxonomyLayout):
    model = Country
    inlines = [
        MetaDataCountryLayout,
    ]


"""
Register taxonomies to show up in admin.
"""
admin.site.register(Country, TaxonomyCountryLayout)
