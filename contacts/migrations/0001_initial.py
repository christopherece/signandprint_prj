# Generated by Django 5.1.6 on 2025-02-24 22:27

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('items', models.CharField(max_length=250)),
                ('item_id', models.IntegerField()),
                ('name', models.CharField(max_length=250)),
                ('email', models.EmailField(blank=True, max_length=150, null=True)),
                ('phone', models.IntegerField(blank=True, max_length=50, null=True)),
                ('message', models.TextField(blank=True)),
                ('contact_date', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('user_id', models.IntegerField(blank=True)),
            ],
        ),
    ]
