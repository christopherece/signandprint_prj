# Generated by Django 5.1.6 on 2025-02-24 01:16

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='service',
            old_name='title',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='service',
            old_name='price',
            new_name='price_max',
        ),
        migrations.AddField(
            model_name='service',
            name='price_min',
            field=models.DecimalField(decimal_places=2, default=4, max_digits=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='service',
            name='usage',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='service',
            name='size',
            field=models.CharField(max_length=50),
        ),
        migrations.CreateModel(
            name='ServiceFeature',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('feature', models.CharField(max_length=255)),
                ('service', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='features', to='services.service')),
            ],
        ),
        migrations.CreateModel(
            name='ServiceGallery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='services/gallery/')),
                ('service', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='gallery', to='services.service')),
            ],
        ),
    ]
