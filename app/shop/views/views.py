from django.views.generic import TemplateView
from django.shortcuts import render


class AddressView(TemplateView):
    template_name = 'shop/profile-address.html'

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


class ProfileView(TemplateView):
    template_name = 'shop/profile.html'

    def get(self, request):
        context = {}
        return render(request, self.template_name, context)


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
