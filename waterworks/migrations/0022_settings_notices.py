# Generated by Django 3.1.6 on 2021-03-02 16:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('waterworks', '0021_modem'),
    ]

    operations = [
        migrations.AddField(
            model_name='settings',
            name='notices',
            field=models.CharField(default='', max_length=1000),
        ),
    ]