# Generated by Django 3.0.10 on 2020-10-02 12:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('taxonomies', '0002_currency_countries'),
    ]

    operations = [
        migrations.AlterField(
            model_name='currency',
            name='countries',
            field=models.ManyToManyField(related_name='currency', to='taxonomies.Country', verbose_name='countries'),
        ),
    ]
