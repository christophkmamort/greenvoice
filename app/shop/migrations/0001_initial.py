# Generated by Django 3.0.8 on 2020-08-08 05:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=200, verbose_name='name')),
                ('status', models.PositiveSmallIntegerField(choices=[(1, 'draft'), (2, 'published'), (3, 'paused'), (4, 'retired')], default=1, verbose_name='status')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='created')),
            ],
            options={
                'ordering': ['created'],
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=200, verbose_name='title')),
                ('price', models.FloatField(blank=True, verbose_name='price')),
                ('image', models.ImageField(blank=True, upload_to='', verbose_name='image')),
                ('status', models.PositiveSmallIntegerField(choices=[(1, 'draft'), (2, 'published'), (3, 'paused'), (4, 'retired')], default=1, verbose_name='status')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='created')),
                ('brand', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='products', to='shop.Brand', verbose_name='brand')),
            ],
            options={
                'ordering': ['created'],
            },
        ),
    ]
