# Generated by Django 3.0.9 on 2020-08-28 11:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0020_auto_20200827_1621'),
    ]

    operations = [
        migrations.CreateModel(
            name='BaseImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='BaseTaxonomy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, null=True, verbose_name='name')),
                ('slug', models.SlugField(null=True, unique=True, verbose_name='slug')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='created')),
            ],
        ),
        migrations.CreateModel(
            name='ProductOption',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_number', models.CharField(blank=True, max_length=200, verbose_name='product number')),
                ('stock', models.IntegerField(blank=True, default=0, verbose_name='stock')),
                ('gross', models.FloatField(blank=True, verbose_name='price gross')),
                ('tax', models.FloatField(blank=True, verbose_name='price tax')),
                ('net', models.FloatField(blank=True, verbose_name='price net')),
                ('status', models.PositiveSmallIntegerField(choices=[(1, 'draft'), (2, 'published'), (3, 'paused'), (4, 'retired')], default=1, verbose_name='status')),
                ('value', models.FloatField(default=0, max_length=200, verbose_name='value')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='created')),
            ],
        ),
        migrations.AlterModelOptions(
            name='product',
            options={},
        ),
        migrations.RemoveField(
            model_name='product',
            name='image',
        ),
        migrations.RemoveField(
            model_name='product',
            name='price',
        ),
        migrations.RemoveField(
            model_name='product',
            name='status',
        ),
        migrations.RemoveField(
            model_name='product',
            name='value',
        ),
        migrations.CreateModel(
            name='Color',
            fields=[
                ('basetaxonomy_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='shop.BaseTaxonomy')),
            ],
            bases=('shop.basetaxonomy',),
        ),
        migrations.CreateModel(
            name='ProductBrandImage',
            fields=[
                ('baseimage_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='shop.BaseImage')),
                ('image', models.ImageField(blank=True, upload_to='products/brands/', verbose_name='image')),
            ],
            bases=('shop.baseimage',),
        ),
        migrations.CreateModel(
            name='ProductImage',
            fields=[
                ('baseimage_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='shop.BaseImage')),
                ('image', models.ImageField(blank=True, upload_to='products/', verbose_name='image')),
            ],
            bases=('shop.baseimage',),
        ),
        migrations.CreateModel(
            name='Size',
            fields=[
                ('basetaxonomy_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='shop.BaseTaxonomy')),
            ],
            bases=('shop.basetaxonomy',),
        ),
        migrations.AddField(
            model_name='product',
            name='options',
            field=models.ManyToManyField(blank=True, to='shop.ProductOption', verbose_name='options'),
        ),
        migrations.AddField(
            model_name='productoption',
            name='brand_gallery',
            field=models.ManyToManyField(blank=True, to='shop.ProductBrandImage', verbose_name='brand gallery'),
        ),
        migrations.AddField(
            model_name='productoption',
            name='color',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='shop.Color', verbose_name='color'),
        ),
        migrations.AddField(
            model_name='productoption',
            name='gallery',
            field=models.ManyToManyField(blank=True, to='shop.ProductImage', verbose_name='gallery'),
        ),
        migrations.AddField(
            model_name='productoption',
            name='size',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='shop.Size', verbose_name='size'),
        ),
    ]
