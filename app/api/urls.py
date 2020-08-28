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
router.register(r'product-brand-gallery', views.ProductBrandGalleryViewSet, basename='product-brand-gallery')
router.register(r'product-gallery', views.ProductGalleryViewSet, basename='product-gallery')
router.register(r'product-option', views.ProductOptionViewSet, basename='product-option')
router.register(r'size', views.SizeViewSet, basename='size')
router.register(r'users', views.UserViewSet, basename='user')
router.register(r'value-log', views.ValueLogViewSet, basename='value-log')

# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls')),
]


# New: ProductOption
