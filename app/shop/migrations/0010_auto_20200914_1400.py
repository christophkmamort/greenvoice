# Generated by Django 3.0.10 on 2020-09-14 14:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
        ('shop', '0009_auto_20200912_1504'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='wishlistitem',
            name='product_option',
        ),
        migrations.AlterField(
            model_name='orderitem',
            name='customer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='users.Customer', verbose_name='customer'),
        ),
        migrations.AlterField(
            model_name='orderitem',
            name='order',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='order_items', to='shop.Order', verbose_name='order'),
        ),
        migrations.AlterField(
            model_name='orderitem',
            name='product_option',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='shop.ProductOption', verbose_name='product'),
        ),
    ]
