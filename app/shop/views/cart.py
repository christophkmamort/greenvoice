from django.views.generic import TemplateView
from django.shortcuts import render


class CartView(TemplateView):
    template_name = 'shop/cart.html'

    def get(self, request):
        context = {}
        return render(request, self.template_name, context)
