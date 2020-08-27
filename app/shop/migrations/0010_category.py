# Generated by Django 3.0.8 on 2020-08-24 06:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0009_orderitem_customer'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, null=True, verbose_name='name')),
                ('slug', models.SlugField(null=True, unique=True, verbose_name='slug')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='created')),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='shop.Category', verbose_name='parent')),
            ],
            options={
                'unique_together': {('slug', 'parent')},
            },
        ),
    ]