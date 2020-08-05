from django.urls import path

from . import views

app_name = 'shop'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('shop', views.ShopView.as_view(), name='shop'),

    path('login', views.LoginView.as_view(), name='login'),
    path('order', views.OrderView.as_view(), name='order'),
    path('profile', views.ProfileView.as_view(), name='profile'),
    path('profile/address', views.AddressView.as_view(), name='address'),
    path('profile/edit', views.EditView.as_view(), name='edit'),
    path('profile/orders', views.OrdersView.as_view(), name='orders'),
    path('profile/payment-methods', views.PaymentMethodsView.as_view(), name='payment-methods'),
    path('refund', views.RefundView.as_view(), name='refund'),
    path('register', views.RegisterView.as_view(), name='register'),
    path('shop/cart', views.CartView.as_view(), name='cart'),
    path('shop/checkout', views.CheckoutView.as_view(), name='checkout'),
    path('shop/product', views.ProductView.as_view(), name='product'),
    path('shop/wishlist', views.WishlistView.as_view(), name='wishlist'),
]
