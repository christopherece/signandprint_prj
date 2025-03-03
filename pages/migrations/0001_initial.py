# Generated by Django 5.1.6 on 2025-02-24 10:18

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
                ('name', models.CharField(max_length=250)),
                ('email', models.EmailField(blank=True, max_length=150, null=True)),
                ('phone', models.IntegerField(blank=True, max_length=50, null=True)),
                ('subject', models.TextField()),
                ('category', models.CharField(choices=[('signage', 'Signage'), ('display_signs', 'Display Signs'), ('digital_printing', 'Digital Printing'), ('vehicle_signs', 'Vehicle Signs')], default='Please select Service', max_length=150)),
                ('description', models.TextField()),
            ],
        ),
    ]
