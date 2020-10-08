from django.contrib import admin
from django.utils.translation import gettext_lazy as _

from taxonomies.models.iso_coded import *


"""
Basic taxonomy layout.
"""
class BasicTaxonomyLayout(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}


"""
Country layout.
"""
class MetaDataCountryLayout(admin.StackedInline):
    model = MetaDataCountry


class CountryLayout(BasicTaxonomyLayout):
    model = Country
    inlines = [
        MetaDataCountryLayout,
    ]


admin.site.register(Country, CountryLayout)


"""
Company type layout.
"""
class MetaDataCompanyTypeLayout(admin.StackedInline):
    model = MetaDataCompanyType


class CompanyTypeLayout(BasicTaxonomyLayout):
    model = CompanyType
    inlines = [
        MetaDataCompanyTypeLayout,
    ]


admin.site.register(CompanyType, CompanyTypeLayout)


"""
Currency layout.
"""
class MetaDataCurrencyLayout(admin.StackedInline):
    model = MetaDataCurrency


class CurrencyLayout(BasicTaxonomyLayout):
    model = Currency
    inlines = [
        MetaDataCurrencyLayout,
    ]


admin.site.register(Currency, CurrencyLayout)
