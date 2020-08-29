from django.urls import path, include
from rest_framework.routers import DefaultRouter

from . import views

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'brand', views.BrandViewSet, basename='brand')
router.register(r'category', views.CategoryViewSet, basename='category')
router.register(r'color', views.ColorViewSet, basename='color')
router.register(r'customer', views.CustomerViewSet, basename='customer')
router.register(r'order', views.OrderViewSet, basename='order')
router.register(r'order-item', views.OrderItemViewSet, basename='orderitem')
router.register(r'product', views.ProductViewSet, basename='product')
router.register(r'product-brand-image', views.ProductBrandImageViewSet, basename='product-brand-image')
router.register(r'product-image', views.ProductImageViewSet, basename='product-image')
router.register(r'product-option', views.ProductOptionViewSet, basename='product-option')
router.register(r'product-manager', views.ProductManagerViewSet, basename='product-manager')
router.register(r'size', views.SizeViewSet, basename='size')
router.register(r'users', views.UserViewSet, basename='user')
router.register(r'brand-value-log', views.BrandValueLogViewSet, basename='brand-value-log')
router.register(r'product-value-log', views.ProductValueLogViewSet, basename='product-value-log')
router.register(r'taxonomy-value-log', views.TaxonomyValueLogViewSet, basename='taxonomy-value-log')

# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls')),
]
