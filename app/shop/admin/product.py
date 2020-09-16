from django.contrib import admin
from nested_inline.admin import NestedStackedInline, NestedModelAdmin
from django.utils.translation import gettext_lazy as _

from shop.models.media import ProductImage, ProductBrandImage
from shop.models.product import Product, ProductManager, ProductOption


class ProductImageInline(NestedStackedInline):
    model = ProductImage
    extra = 1
    verbose_name = _('image')


class ProductOptionInline(NestedStackedInline):
    model = ProductOption
    extra = 1
    verbose_name = _('option')


class ProductBrandImageInline(NestedStackedInline):
    model = ProductBrandImage
    extra = 1
    verbose_name = _('brand image')


class ProductManagerInline(NestedStackedInline):
    model = ProductManager
    extra = 1
    inlines = [
        ProductImageInline,
        ProductOptionInline,
        ProductBrandImageInline,
    ]
    verbose_name = _('color')


class ProductLayout(NestedModelAdmin):
    model = Product
    inlines = [
        ProductManagerInline,
    ]


admin.site.register(Product, ProductLayout)
