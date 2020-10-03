# Generated by Django 3.0.10 on 2020-10-03 14:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0008_auto_20201003_1423'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='brand',
            name='imprint',
        ),
        migrations.AlterField(
            model_name='basicimprint',
            name='line_2',
            field=models.CharField(blank=True, max_length=200, verbose_name='line 2'),
        ),
        migrations.CreateModel(
            name='BrandImprint',
            fields=[
                ('basicimprint_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='shop.BasicImprint')),
                ('brand', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='imprint', to='shop.Brand', verbose_name='brand')),
            ],
            bases=('shop.basicimprint',),
        ),
    ]
