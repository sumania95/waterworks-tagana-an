# Generated by Django 3.1.6 on 2021-02-21 15:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('waterworks', '0004_auto_20210221_1504'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='barangay',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='waterworks.barangay'),
        ),
    ]
