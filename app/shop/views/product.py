from django.views.generic import TemplateView
from django.shortcuts import render

from shop.models.log import ValueLog
from shop.models.brand import Brand
from shop.models.product import Product
from shop.models.taxonomies import Category


class ProductView(TemplateView):
    template_name = 'shop/product.html'

    def get(self, request, pk):
        # products = Product.objects.all()
        product = Product.objects.get(id=pk)
        brand = Brand.objects.get(product=product)

        # Value log
        ValueLog.objects.create(product=product, action=1)
        ValueLog.objects.create(brand=brand, action=1)

        productVal = 0
        productLogs = ValueLog.objects.filter(product=pk)
        for log in productLogs:
            productVal += log.get_value
        product.value = productVal
        product.save()

        brandVal = 0
        brandLogs = ValueLog.objects.filter(brand=brand)
        for log in brandLogs:
            brandVal += log.get_value
        brand.value = brandVal
        brand.save()

        # Category log logic

        context = {'product':product,} # 'products':products
        return render(request, self.template_name, context)
