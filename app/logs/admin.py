from django.contrib import admin
from django.utils.translation import gettext_lazy as _

from .models import BrandValueLog, ProductValueLog, TaxonomyValueLog


admin.site.register(BrandValueLog)
admin.site.register(ProductValueLog)
admin.site.register(TaxonomyValueLog)
