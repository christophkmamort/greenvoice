# Generated by Django 3.0.8 on 2020-08-08 10:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_customer'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='email',
        ),
    ]