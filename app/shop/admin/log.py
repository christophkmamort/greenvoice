from django.contrib import admin
from django.utils.translation import gettext_lazy as _

from shop.models.log import ProductLog


admin.site.register(ProductLog)
