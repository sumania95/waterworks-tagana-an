# Generated by Django 3.1.6 on 2021-02-25 23:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('waterworks', '0012_settings_water_meter'),
    ]

    operations = [
        migrations.RenameField(
            model_name='settings',
            old_name='water_meter',
            new_name='water_meter_charge',
        ),
    ]
