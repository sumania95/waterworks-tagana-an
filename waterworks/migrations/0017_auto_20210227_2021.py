# Generated by Django 3.1.6 on 2021-02-27 20:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('waterworks', '0016_auto_20210226_2031'),
    ]

    operations = [
        migrations.AddField(
            model_name='meter_installation',
            name='cluster',
            field=models.CharField(default='0000', max_length=200),
        ),
        migrations.AddField(
            model_name='meter_installation',
            name='sequence',
            field=models.CharField(default='0000', max_length=200),
        ),
    ]
