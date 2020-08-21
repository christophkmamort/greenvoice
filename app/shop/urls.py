from django.urls import path

from . import views

app_name = 'shop'
urlpatterns = [
    # Shop
    path('', views.IndexView.as_view(), name='index'),
    path('login', views.LoginView.as_view(), name='login'),
    path('logout', views.LogoutView.as_view(), name='logout'),
    path('order', views.OrderView.as_view(), name='order'),
    path('profile', views.ProfileView.as_view(), name='profile'),
    path('profile/address', views.AddressView.as_view(), name='address'),
    path('profile/edit', views.EditView.as_view(), name='edit'),
    path('profile/orders', views.OrdersView.as_view(), name='orders'),
    path('profile/payment-methods', views.PaymentMethodsView.as_view(), name='payment-methods'),
    path('refund', views.RefundView.as_view(), name='refund'),
    path('register', views.RegisterView.as_view(), name='register'),
    path('shop', views.ShopView.as_view(), name='shop'),
    path('shop/cart', views.CartView.as_view(), name='cart'),
    path('shop/checkout', views.CheckoutView.as_view(), name='checkout'),
    path('shop/product/<int:pk>', views.ProductView.as_view(), name='product'),
    path('shop/wishlist', views.WishlistView.as_view(), name='wishlist'),
    path('terms', views.TermsView.as_view(), name='terms'),

    # Shop (functional)
    path('shop/update-cart/', views.updateCart, name='update-cart'),
    path('test', views.TestView.as_view(), name='test'),

    # Legal
    path('imprint', views.ImprintView.as_view(), name='imprint'),
    path('privacy', views.PrivacyView.as_view(), name='privacy'),

    # Business links (add to business.greenvoice.shop domain)
    path('business/terms-of-sale', views.TermsOfSaleView.as_view(), name='terms-of-sale'),
    path('business/shooting-agreements', views.ShootingAgreementsView.as_view(), name='shooting-agreements')
]
