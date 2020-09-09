# Generated by Django 3.0.10 on 2020-09-09 14:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0007_auto_20200909_1345'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='basevaluelog',
            name='user',
        ),
        migrations.RemoveField(
            model_name='brandvaluelog',
            name='basevaluelog_ptr',
        ),
        migrations.RemoveField(
            model_name='brandvaluelog',
            name='brand',
        ),
        migrations.RemoveField(
            model_name='productvaluelog',
            name='basevaluelog_ptr',
        ),
        migrations.RemoveField(
            model_name='productvaluelog',
            name='product',
        ),
        migrations.RemoveField(
            model_name='productvaluelog',
            name='product_manager',
        ),
        migrations.RemoveField(
            model_name='productvaluelog',
            name='product_option',
        ),
        migrations.RemoveField(
            model_name='taxonomyvaluelog',
            name='basevaluelog_ptr',
        ),
        migrations.RemoveField(
            model_name='taxonomyvaluelog',
            name='category',
        ),
        migrations.RemoveField(
            model_name='taxonomyvaluelog',
            name='color',
        ),
        migrations.RemoveField(
            model_name='taxonomyvaluelog',
            name='size',
        ),
        migrations.DeleteModel(
            name='AnonymousUserData',
        ),
        migrations.DeleteModel(
            name='BaseValueLog',
        ),
        migrations.DeleteModel(
            name='BrandValueLog',
        ),
        migrations.DeleteModel(
            name='ProductValueLog',
        ),
        migrations.DeleteModel(
            name='TaxonomyValueLog',
        ),
    ]
