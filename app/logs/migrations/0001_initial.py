# Generated by Django 3.0.10 on 2020-09-10 11:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('taxonomies', '0001_initial'),
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AnonymousUserData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.CharField(blank=True, max_length=200, verbose_name='city')),
                ('country', models.CharField(blank=True, max_length=200, verbose_name='country')),
                ('gender', models.PositiveSmallIntegerField(blank=True, choices=[(1, 'women'), (2, 'men')], verbose_name='gender')),
                ('language', models.CharField(blank=True, max_length=200, verbose_name='language')),
                ('referer', models.CharField(blank=True, max_length=200, verbose_name='referer')),
                ('state', models.CharField(blank=True, max_length=200, verbose_name='state')),
                ('body_measurements', models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='users.BodyMeasurements', verbose_name='body measurements')),
            ],
        ),
        migrations.CreateModel(
            name='BaseValueLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('action', models.PositiveSmallIntegerField(choices=[(1, 'click'), (2, 'wishlist'), (3, 'cart'), (4, 'order')], default=1, verbose_name='action')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='created')),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='logs.AnonymousUserData', verbose_name='anonymous user data')),
            ],
        ),
        migrations.CreateModel(
            name='BrandValueLog',
            fields=[
                ('basevaluelog_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='logs.BaseValueLog')),
            ],
            options={
                'verbose_name': 'brand log',
            },
            bases=('logs.basevaluelog',),
        ),
        migrations.CreateModel(
            name='ProductValueLog',
            fields=[
                ('basevaluelog_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='logs.BaseValueLog')),
            ],
            options={
                'verbose_name': 'product log',
            },
            bases=('logs.basevaluelog',),
        ),
        migrations.CreateModel(
            name='TaxonomyValueLog',
            fields=[
                ('basevaluelog_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='logs.BaseValueLog')),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='taxonomies.Category', verbose_name='category')),
                ('color', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='taxonomies.Color', verbose_name='color')),
                ('size', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='taxonomies.Size', verbose_name='size')),
            ],
            options={
                'verbose_name': 'taxonomy log',
            },
            bases=('logs.basevaluelog',),
        ),
    ]
