from django.db import models
from django.utils.translation import gettext_lazy as _

from .brand import Brand
from .basic import BasicStatus
from taxonomies.models.categories import Category, TargetGroup
from taxonomies.models.options import Color, Size


class Product(models.Model):
    brand = models.ForeignKey(Brand, blank=True, on_delete=models.CASCADE, related_name='product', verbose_name=_('brand'))
    category = models.ManyToManyField(Category, blank=True, verbose_name=_('category'))
    created = models.DateTimeField(auto_now_add=True, verbose_name=_('created'))
    name = models.CharField(max_length=200, blank=True, verbose_name=_('name'))
    target_group = models.ManyToManyField(TargetGroup, blank=True, verbose_name=_('target group'))
    # TODO: Add transparency manager here!!

    def save(self, *args, **kwargs):
        product_managers = self.product_manager.all()
        if product_managers:
            for product_manager in product_managers:
                query = ''
                categories = self.category.all()
                if categories:
                    for category in categories:
                        query += category.name + ' '
                target_groups = self.target_group.all()
                if target_groups:
                    for target_group in target_groups:
                        if target_group.name == 'Unisex':
                            query += 'Unisex Frauen Damen Herren Männer '
                        elif target_group.name == 'Woman':
                            query += 'Frauen Damen '
                        elif target_group.name == 'Men':
                            query += 'Herren Männer '
                product_manager.query = query
                product_manager.save()

                """ product_brand_images = product_manager.brand_image.all()
                if product_brand_images:
                    for product_brand_image in product_brand_images:
                        product_brand_image = product_brand_image.image
                        if product_brand_image:
                            width = 640
                            if product_brand_image.size[0] > width:
                                hpercent = (width / float(product_brand_image.size[0]))
                                height = int(product_brand_image.size[1] * float(hpercent))
                                size = (width, height)
                                product_brand_image = product_brand_image.resize(size, resample=0, box=None)
                            thumb_io = BytesIO()
                            product_brand_image.save(thumb_io, format='JPEG', optimize=True, quality=50)
                            inmemory_uploaded_file = InMemoryUploadedFile(thumb_io, None, product_brand_image.name.split(
                                '.')[0] + '.jpg', 'image/jpeg', thumb_io.tell(), None)
                            product_brand_image = inmemory_uploaded_file """

        super(Product, self).save(*args, **kwargs)


class ProductManager(models.Model):
    color = models.ForeignKey(Color, blank=True, null=True, on_delete=models.SET_NULL, verbose_name=_('color'))
    created = models.DateTimeField(auto_now_add=True, verbose_name=_('created'))
    product = models.ForeignKey(Product, null=True, on_delete=models.CASCADE, related_name='product_manager', verbose_name=_('product'))
    query = models.CharField(max_length=200, blank=True, verbose_name=_('queryset'))
    # TODO: Add transparency manager here!!
    value = models.FloatField(max_length=200, default=0, verbose_name=_('value'))


class ProductOption(models.Model):
    created = models.DateTimeField(auto_now_add=True, verbose_name=_('created'))
    price = models.FloatField(blank=True, null=True, verbose_name=_('price (gross)'))
    product_manager = models.ForeignKey(ProductManager, null=True, on_delete=models.CASCADE, related_name='product_option', verbose_name=_('product and color'))
    product_number = models.CharField(max_length=200, blank=True, null=True, verbose_name=_('product number'))
    size = models.ForeignKey(Size, blank=True, null=True, on_delete=models.SET_NULL, verbose_name=_('size'))
    # TODO: Add stock manager here!!
    # TODO: Add transparency manager here!!


class ProductStatus(BasicStatus):
    product = models.ForeignKey(Product, null=True, on_delete=models.CASCADE, related_name='status', verbose_name=_('product'))


class ProductManagerStatus(BasicStatus):
    product_manager = models.ForeignKey(ProductManager, null=True, on_delete=models.CASCADE, related_name='status', verbose_name=_('product manager'))


class ProductOptionStatus(BasicStatus):
    product_option = models.ForeignKey(ProductOption, null=True, on_delete=models.CASCADE, related_name='status', verbose_name=_('product option'))
