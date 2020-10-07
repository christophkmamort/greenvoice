from django.urls import path, include
from rest_framework.routers import DefaultRouter
# from rest_framework_nested import routers

from . import views


router = DefaultRouter() # routers.SimpleRouter()

router.register(r'brand', views.BrandViewSet, basename='brand')
router.register(r'taxonomy/country', views.CountryViewSet, basename='taxonomy-country')
router.register(r'taxonomy/company-type', views.CompanyTypeViewSet, basename='taxonomy-company-type')
router.register(r'taxonomy/currency', views.CurrencyViewSet, basename='taxonomy-currency')

""" router.register(r'log-brand', views.BrandValueLogViewSet, basename='log-brand')
router.register(r'log-product', views.ProductValueLogViewSet, basename='log-product')
router.register(r'log-taxonomy', views.TaxonomyValueLogViewSet, basename='log-taxonomy') """

""" router.register(r'order', views.OrderViewSet, basename='order')
router.register(r'order-item', views.OrderItemViewSet, basename='order-item')

router.register(r'product', views.ProductViewSet, basename='product')
router.register(r'product-manager', views.ProductManagerViewSet, basename='product-manager')
router.register(r'product-manager-brand-image', views.ProductBrandImageViewSet, basename='product-manger-brand-image')
router.register(r'product-manager-image', views.ProductImageViewSet, basename='product-manger-image')
router.register(r'product-option', views.ProductOptionViewSet, basename='product-option')

router.register(r'taxonomy-category', views.CategoryViewSet, basename='taxonomy-category')
router.register(r'taxonomy-color', views.ColorViewSet, basename='taxonomy-color')
router.register(r'taxonomy-country', views.CountryViewSet, basename='taxonomy-country')
router.register(r'taxonomy-size', views.SizeViewSet, basename='taxonomy-size')
router.register(r'taxonomy-target-group', views.TargetGroupViewSet, basename='taxonomy-target-group')

router.register(r'user', views.UserViewSet, basename='user')
router.register(r'user-customer', views.CustomerViewSet, basename='user-customer')

router.register(r'wishlist-item', views.WishlistItemViewSet, basename='wishlist-item') """

# https://github.com/alanjds/drf-nested-routers
# taxonomy_router = routers.NestedSimpleRouter(router, r'taxonomy', lookup='taxonomy') # taxonomy_router = DefaultRouter()
# taxonomy_router.register(r'country', views.CountryViewSet, basename='taxonomy-country')
# taxonomy_router.register(r'company-type', views.CompanyTypeViewSet, basename='taxonomy-company-type')
# taxonomy_router.register(r'currency', views.CurrencyViewSet, basename='taxonomy-currency')

# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('', include(router.urls)), # url(r'^', include(router.urls)),
    path('api-auth/', include('rest_framework.urls')),
]
