from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.views.generic import TemplateView
from django.shortcuts import render, redirect

from users.forms import CustomUserCreationForm


class AddressView(TemplateView):
    template_name = 'shop/profile-address.html'

    def get(self, request):
        context = {}
        return render(request, self.template_name, context)


class CartView(TemplateView):
    template_name = 'shop/cart.html'

    def get(self, request):
        context = {}
        return render(request, self.template_name, context)


class CheckoutView(TemplateView):
    template_name = 'shop/checkout.html'

    def get(self, request):
        context = {}
        return render(request, self.template_name, context)


class EditView(TemplateView):
    template_name = 'shop/profile-edit.html'

    def get(self, request):
        context = {}
        return render(request, self.template_name, context)


class ImprintView(TemplateView):
    template_name = 'shop/imprint.html'

    def get(self, request):
        context = {}
        return render(request, self.template_name, context)


class IndexView(TemplateView):
    template_name = 'shop/index.html'

    def get(self, request):
        context = {}
        return render(request, self.template_name, context)


class LoginView(TemplateView):
    template_name = 'shop/login.html'

    def get(self, request):
        if request.user.is_authenticated:
            return redirect('shop:index')

        context = {}
        return render(request, self.template_name, context)

    def post(self, request):
        email = request.POST.get('loginEmail')
        password =request.POST.get('loginPassword')

        user = authenticate(request, email=email, password=password)

        if user is not None:
            login(request, user)
            return redirect('shop:index')
        else:
            messages.info(request, 'E-Mail oder Passwort ist falsch.')

        context = {'submittedLoginEmail': email}
        return render(request, self.template_name, context)


class LogoutView(TemplateView):

    def get(self, request):
        logout(request)
        return redirect('shop:login')


class OrderView(TemplateView):
    template_name = 'shop/order.html'

    def get(self, request):
        context = {}
        return render(request, self.template_name, context)


class OrdersView(TemplateView):
    template_name = 'shop/profile-orders.html'

    def get(self, request):
        context = {}
        return render(request, self.template_name, context)


class PaymentMethodsView(TemplateView):
    template_name = 'shop/profile-payment-methods.html'

    def get(self, request):
        context = {}
        return render(request, self.template_name, context)


class PrivacyView(TemplateView):
    template_name = 'shop/privacy.html'

    def get(self, request):
        context = {}
        return render(request, self.template_name, context)


class ProductView(TemplateView):
    template_name = 'shop/product.html'

    def get(self, request):
        context = {}
        return render(request, self.template_name, context)


class ProfileView(TemplateView):
    template_name = 'shop/profile.html'

    def get(self, request):
        context = {}
        return render(request, self.template_name, context)


class RefundView(TemplateView):
    template_name = 'shop/refund.html'

    def get(self, request):
        context = {}
        return render(request, self.template_name, context)


class RegisterView(TemplateView):
    template_name = 'shop/register.html'

    def get(self, request):
        if request.user.is_authenticated:
            return redirect('shop:index')

        form = CustomUserCreationForm()

        context = {'form':form}
        return render(request, self.template_name, context)

    def post(self, request):
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email')
            messages.success(request, 'Account für '+ email +' erfolgreich erstellt.')

            return redirect('shop:login')

        context = {'form':form,}
        return render(request, 'accounts/register.html', context)


class ShootingAgreementsView(TemplateView):
    template_name = 'shop/shooting-agreements.html'

    def get(self, request):
        context = {}
        return render(request, self.template_name, context)


class ShopView(TemplateView):
    template_name = 'shop/shop.html'

    def get(self, request):
        context = {}
        return render(request, self.template_name, context)


class TermsOfSaleView(TemplateView):
    template_name = 'shop/terms-of-sale.html'

    def get(self, request):
        context = {}
        return render(request, self.template_name, context)


class TermsView(TemplateView):
    template_name = 'shop/terms.html'

    def get(self, request):
        context = {}
        return render(request, self.template_name, context)


class WishlistView(TemplateView):
    template_name = 'shop/wishlist.html'

    def get(self, request):
        context = {}
        return render(request, self.template_name, context)
