# Generated by Django 3.0.10 on 2020-09-10 10:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_auto_20200910_1015'),
    ]

    operations = [
        migrations.AddField(
            model_name='productmanager',
            name='query',
            field=models.CharField(blank=True, max_length=200, verbose_name='queryset'),
        ),
    ]
