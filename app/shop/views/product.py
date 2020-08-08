from django.views.generic import TemplateView
from django.shortcuts import render

from shop.models.product import Product


class ProductView(TemplateView):
    template_name = 'shop/product.html'

    def get(self, request, pk):
        products = Product.objects.all()
        product = Product.objects.get(id=pk)

        context = {
            'product':product,
            'products':products}
        return render(request, self.template_name, context)
