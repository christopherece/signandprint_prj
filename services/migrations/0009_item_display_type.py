# Generated by Django 5.1.6 on 2025-02-24 09:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0008_item'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='display_type',
            field=models.CharField(choices=[('signage', 'Signage'), ('display_design', 'Display Design'), ('digital_printing', 'Digital Printing'), ('vehicle_signs', 'Vehicle Signs')], default='signage', max_length=50),
        ),
    ]
