from django.contrib import admin
from nested_inline.admin import NestedStackedInline, NestedModelAdmin
from django.utils.translation import gettext_lazy as _

from shop.models.product import Product, ProductManager, ProductOption


class ProductOptionInline(NestedStackedInline):
    # fields = '__all__'
    model = ProductOption
    extra = 1
    # readonly_fields = ['timestamp',]
    # fk_name = 'order_product'
    # verbose_name = _('status')
    # verbose_name_plural = _('events')


class ProductManagerInline(NestedStackedInline):
    # fields = '__all__'
    model = ProductManager
    extra = 1
    inlines = [
        ProductOptionInline,
    ]

class ProductLayout(NestedModelAdmin):
    # fields = '__all__'
    model = Product
    extra = 1
    inlines = [
        ProductManagerInline,
    ]



admin.site.register(Product, ProductLayout)
# admin.site.register(ProductManager)
# admin.site.register(ProductOption)
