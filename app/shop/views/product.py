from django.views.generic import TemplateView
from django.shortcuts import render

from shop.models.log import ProductLog
from shop.models.product import Product


class ProductView(TemplateView):
    template_name = 'shop/product.html'

    def get(self, request, pk):
        products = Product.objects.all()
        product = Product.objects.get(id=pk)

        # Log click
        ProductLog.objects.create(product=product, action=1)
        logs = ProductLog.objects.filter(product=pk)
        value = 0
        for log in logs:
            value += log.get_value
        product.value = value
        product.save()

        context = {
            'product':product,
            'products':products}
        return render(request, self.template_name, context)
