# Generated by Django 5.1.6 on 2025-02-24 01:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0004_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='service',
            name='type',
            field=models.CharField(choices=[('signage', 'Signage'), ('display_signs', 'Display Signs'), ('digital_printing', 'Digital Printing'), ('vehicle_signs', 'Vehicle Signs')], default='signage', max_length=50),
        ),
    ]
