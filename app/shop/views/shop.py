from django.views.generic import TemplateView
from django.shortcuts import render

from shop.models.brand import Brand
from logs.models import BrandValueLog, ProductValueLog, TaxonomyValueLog
from shop.models.product import Product
from taxonomies.models import Category


class IndexView(TemplateView):
    template_name = 'shop/index.html'

    def get(self, request):
        products = Product.objects.all()
        context = {'products':products}
        return render(request, self.template_name, context)


class ShopView(TemplateView):
    template_name = 'shop/shop.html'

    """def get(self, request):
        try:
            category = Category.objects.get(name=request.GET.get('category', ''))

            ValueLog.objects.create(category=category, action=1)

            categoryVal = 0
            categoryLogs = ValueLog.objects.filter(category=category)
            for log in categoryLogs:
                categoryVal += log.get_value
            category.value = categoryVal
            category.save()

            products = Product.objects.filter(category=category)
            for product in products:
                ValueLog.objects.create(product=product, action=1)

                productVal = 0
                productLogs = ValueLog.objects.filter(product=product)
                for log in productLogs:
                    productVal += log.get_value
                product.value = productVal
                product.save()

                brand = Brand.objects.get(product=product)

                ValueLog.objects.create(brand=brand, action=1)

                brandVal = 0
                brandLogs = ValueLog.objects.filter(brand=brand)
                for log in brandLogs:
                    brandVal += log.get_value
                brand.value = brandVal
                brand.save()
        except:
            pass

        context = {}
        return render(request, self.template_name, context)"""
