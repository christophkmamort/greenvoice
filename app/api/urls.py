from django.urls import path
from . import views

urlpatterns = [
	path('', views.apiOverview, name="api"),
	path('product-list/', views.productList, name="product-list"),
	path('product-datail/<str:pk>/', views.productDetail, name="product-datail"),
	path('product-create/', views.productCreate, name="product-create"),
	path('product-update/<str:pk>/', views.productUpdate, name="product-update"),
	path('product-delete/<str:pk>/', views.productDelete, name="product-delete"),
]
