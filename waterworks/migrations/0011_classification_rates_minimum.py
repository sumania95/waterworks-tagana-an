# Generated by Django 3.1.6 on 2021-02-25 21:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('waterworks', '0010_auto_20210225_2039'),
    ]

    operations = [
        migrations.AddField(
            model_name='classification_rates',
            name='minimum',
            field=models.BooleanField(default=False),
        ),
    ]
