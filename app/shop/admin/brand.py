from django.contrib import admin
from django.utils.translation import gettext_lazy as _

from shop.models.brand import *


class BrandImprintLayout(admin.StackedInline):
    model = BrandImprint


class BrandLayout(admin.ModelAdmin):
    model = Brand
    inlines = [
        BrandImprintLayout,
    ]


admin.site.register(Brand, BrandLayout)
