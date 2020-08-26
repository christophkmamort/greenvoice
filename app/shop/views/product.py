from django.views.generic import TemplateView
from django.shortcuts import render

from shop.models.brand import Brand
from shop.models.log import ValueLog
from shop.models.product import Product
from shop.models.taxonomies import Category


class ProductView(TemplateView):
    template_name = 'shop/product.html'

    def get(self, request, pk):
        product = Product.objects.get(id=pk)
        brand = Brand.objects.get(product=product)

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

        for categoryName in product.category.all():
            category = Category.objects.get(name=categoryName)
            ValueLog.objects.create(category=category, action=1)

            categoryVal = 0
            categoryLogs = ValueLog.objects.filter(category=category)
            for log in categoryLogs:
                categoryVal += log.get_value
            category.value = categoryVal
            category.save()

        context = {'product':product,}
        return render(request, self.template_name, context)
