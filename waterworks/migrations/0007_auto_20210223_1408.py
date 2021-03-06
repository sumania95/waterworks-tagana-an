# Generated by Django 3.1.6 on 2021-02-23 14:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('waterworks', '0006_auto_20210223_0013'),
    ]

    operations = [
        migrations.AddField(
            model_name='meter_replace',
            name='old_meter_no',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AddField(
            model_name='meter_replace',
            name='old_reading',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='activity_logs',
            name='logs',
            field=models.CharField(choices=[('1', 'Information Changed'), ('2', 'Intalled Water Meter'), ('3', 'Replace Water Meter')], default=1, max_length=200),
        ),
        migrations.AlterField(
            model_name='user_logs',
            name='user_logs',
            field=models.CharField(choices=[('1', 'Information Changed'), ('2', 'Intalled Water Meter'), ('3', 'Replace Water Meter')], default=1, max_length=200),
        ),
    ]
