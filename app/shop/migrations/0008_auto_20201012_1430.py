# Generated by Django 3.0.10 on 2020-10-12 14:30

from django.db import migrations, models
import django.db.models.deletion
import shop.models.functions.brand


class Migration(migrations.Migration):

    dependencies = [
        ('taxonomies', '0001_initial'),
        ('shop', '0007_auto_20201012_1403'),
    ]

    operations = [
        migrations.AlterField(
            model_name='brand',
            name='logo',
            field=models.ImageField(blank=True, null=True, unique=True, upload_to=shop.models.functions.brand.brand_branding_upload_path, verbose_name='logo'),
        ),
        migrations.AlterUniqueTogether(
            name='basicimprint',
            unique_together={('line_1', 'line_2', 'post_code', 'city', 'country')},
        ),
        migrations.CreateModel(
            name='BrandImprint',
            fields=[
                ('basicimprint_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='shop.BasicImprint')),
                ('brand', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='imprint', to='shop.Brand', verbose_name='brand')),
            ],
            bases=('shop.basicimprint',),
        ),
    ]
