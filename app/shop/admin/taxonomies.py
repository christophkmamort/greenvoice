from django.contrib import admin
from django.utils.translation import gettext_lazy as _

from shop.models.taxonomies import Category


admin.site.register(Category)
