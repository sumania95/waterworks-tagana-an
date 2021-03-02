# Generated by Django 3.1.6 on 2021-03-02 15:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('waterworks', '0020_auto_20210302_0003'),
    ]

    operations = [
        migrations.CreateModel(
            name='Modem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ip_address', models.CharField(max_length=200)),
                ('username', models.CharField(max_length=200)),
                ('password', models.CharField(max_length=200)),
                ('date_updated', models.DateTimeField(auto_now=True)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
