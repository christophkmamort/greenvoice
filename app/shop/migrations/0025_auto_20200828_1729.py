# Generated by Django 3.0.9 on 2020-08-28 17:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0024_size_order'),
    ]

    operations = [
        migrations.AlterField(
            model_name='size',
            name='order',
            field=models.IntegerField(blank=True, verbose_name='order'),
        ),
    ]
