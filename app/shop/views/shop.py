from django.views.generic import TemplateView
from django.shortcuts import render

from shop.models.product import Product


class IndexView(TemplateView):
    template_name = 'shop/index.html'

    def get(self, request):
        products = Product.objects.all()
        context = {'products':products}
        return render(request, self.template_name, context)
