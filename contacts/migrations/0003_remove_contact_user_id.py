# Generated by Django 5.1.6 on 2025-02-24 23:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0002_rename_items_contact_item'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contact',
            name='user_id',
        ),
    ]
