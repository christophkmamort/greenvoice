from django.contrib import admin
from django.utils.translation import gettext_lazy as _

from shop.models.wishlist import *


admin.site.register(WishlistItem)
