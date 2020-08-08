from django.contrib import admin
from django.utils.translation import gettext_lazy as _

from shop.models.brand import Brand


admin.site.register(Brand)
