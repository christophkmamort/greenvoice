from django.contrib import admin
from django.utils.translation import gettext_lazy as _

from shop.models.gallery import ProductBrandImage, ProductImage


admin.site.register(ProductBrandImage)
admin.site.register(ProductImage)
