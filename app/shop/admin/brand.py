from django.contrib import admin
from nested_inline.admin import NestedStackedInline, NestedModelAdmin
from django.utils.translation import gettext_lazy as _

from shop.models.brand import *


class BrandBrandingLayout(admin.StackedInline):
    model = BrandBranding


class BrandImprintLayout(admin.StackedInline):
    model = BrandImprint


class BrandSettingsSalesLayout(admin.StackedInline):
    model = BrandSettingsSales


class BrandSettingsStatusLayout(admin.StackedInline):
    model = BrandSettingsStatus


class BrandSettingsLayout(admin.StackedInline):
    model = BrandSettings
    inlines = [
        BrandSettingsSalesLayout,
        BrandSettingsStatusLayout,
    ]


class BrandLayout(admin.ModelAdmin):
    model = Brand
    inlines = [
        BrandBrandingLayout,
        BrandImprintLayout,
        BrandSettingsLayout,
    ]


admin.site.register(Brand, BrandLayout)
