from django.contrib import admin
from django.utils.translation import gettext_lazy as _

from shop.models.customer import Customer


admin.site.register(Customer)
