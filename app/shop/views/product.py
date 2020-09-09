from django.views.generic import TemplateView
from django.shortcuts import render

from shop.models.brand import Brand
from logs.models import BrandValueLog, ProductValueLog, TaxonomyValueLog
from shop.models.product import Product, ProductManager, ProductOption
from taxonomies.models import Category, Color, Size


class ProductView(TemplateView):
    template_name = 'shop/product.html'

    def get(self, request, pk):
        product_manager = ProductManager.objects.get(id=pk)
        product = Product.objects.get(id=product_manager.product.id)
        #product_options = ProductOption.objects.filter(product=product)
        """if 1 == 0:
            ProductValueLog.objects.create(product=product, product_manager=product_manager, product_option=product_option, action=1)
        else:"""
        ProductValueLog.objects.create(product=product, product_manager=product_manager, action=1)

        brand = Brand.objects.get(product=product)
        BrandValueLog.objects.create(brand=brand, action=1)

        product_val = 0
        product_logs = ProductValueLog.objects.filter(product=product)
        for log in product_logs:
            product_val += log.get_value
        product.value = product_val
        product.save()

        product_manager_val = 0
        product_manager_logs = ProductValueLog.objects.filter(product_manager=pk)
        for log in product_logs:
            product_manager_val += log.get_value
        product_manager.value = product_manager_val
        product_manager.save()

        """if 1 == 0:
            product_option_val = 0
            product_option_logs = ProductValueLog.objects.filter(product_option=pk)
            for log in product_logs:
                product_option_val += log.get_value
            product_option.value = product_option_val
            product_option.save()"""

        brand_val = 0
        brand_logs = BrandValueLog.objects.filter(brand=brand)
        for log in brand_logs:
            brand_val += log.get_value
        brand.value = brand_val
        brand.save()

        for category_name in product.category.all():
            category = Category.objects.get(name=category_name)
            TaxonomyValueLog.objects.create(category=category, action=1)
            category_val = 0
            category_logs = TaxonomyValueLog.objects.filter(category=category)
            for log in category_logs:
                category_val += log.get_value
            category.value = category_val
            category.save()

        color = Color.objects.get(id=product_manager.color.id)
        TaxonomyValueLog.objects.create(color=color, action=1)
        color_val = 0
        color_logs = TaxonomyValueLog.objects.filter(color=color)
        for log in category_logs:
            color_val += log.get_value
        color.value = color_val
        color.save()

        """if 1 == 0:
            size = Size.objects.get(id=product_option.size.id)
            TaxonomyValueLog.objects.create(size=size, action=1)
            size_val = 0
            size_logs = TaxonomyValueLog.objects.filter(size=size)
            for log in category_logs:
                size_val += log.get_value
            size.value = color_val
            size.save()"""

        context = {}
        return render(request, self.template_name, context)
