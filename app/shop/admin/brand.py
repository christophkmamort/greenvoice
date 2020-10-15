from django.contrib import admin
from nested_inline.admin import NestedStackedInline, NestedModelAdmin
from django.utils.translation import gettext_lazy as _

from shop.models.brand import *


""" class BrandBrandingLayout(NestedStackedInline): # admin.StackedInline
    model = BrandBranding


class BrandImprintLayout(NestedStackedInline): # admin.StackedInline
    model = BrandImprint


class BrandSettingsSalesLayout(NestedStackedInline):  # admin.StackedInline
    model = BrandSettingsSales
    extra = 0


class BrandSettingsStatusLayout(NestedStackedInline):  # admin.StackedInline
    model = BrandSettingsStatus
    extra = 0


class BrandSettingsLayout(NestedStackedInline): # admin.StackedInline
    model = BrandSettings
    inlines = [
        BrandSettingsSalesLayout,
        BrandSettingsStatusLayout,
    ] """


class BrandLayout(admin.ModelAdmin): # admin.StackedInline
    model = Brand
    """ inlines = [
        BrandBrandingLayout,
        BrandImprintLayout,
        BrandSettingsLayout,
    ] """


admin.site.register(Brand, BrandLayout)
