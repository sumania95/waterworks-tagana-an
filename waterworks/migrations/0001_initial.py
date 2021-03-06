# Generated by Django 3.1.6 on 2021-02-21 11:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('middlename', models.CharField(blank=True, max_length=200)),
                ('is_admin', models.BooleanField(default=False)),
                ('is_waterworks_clerk', models.BooleanField(default=False)),
                ('is_collection_clerk', models.BooleanField(default=False)),
                ('date_updated', models.DateTimeField(auto_now=True)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Barangay',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('is_active', models.BooleanField(default=True)),
                ('date_updated', models.DateTimeField(auto_now=True)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Classification',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('date_updated', models.DateTimeField(auto_now=True)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('surname', models.CharField(max_length=200)),
                ('firstname', models.CharField(max_length=200)),
                ('middlename', models.CharField(blank=True, max_length=200)),
                ('barangay', models.CharField(max_length=200)),
                ('service_charge', models.DecimalField(decimal_places=2, default=0, max_digits=50)),
                ('water_meter_charge', models.DecimalField(decimal_places=2, default=0, max_digits=50)),
                ('reconnection_charge', models.DecimalField(decimal_places=2, default=0, max_digits=50)),
                ('date_updated', models.DateTimeField(auto_now=True)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('classification', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='waterworks.classification')),
            ],
            options={
                'ordering': ['surname', 'firstname', 'middlename'],
            },
        ),
        migrations.CreateModel(
            name='Year',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('is_active', models.BooleanField(default=True)),
                ('date_updated', models.DateTimeField(auto_now=True)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='User_Logs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_logs', models.CharField(choices=[('1', 'Account added'), ('2', 'Information Changed'), ('3', 'Intalled Water Meter'), ('4', 'Change Info Water Meter'), ('5', 'Replace Water Meter')], default=1, max_length=200)),
                ('date_updated', models.DateTimeField(auto_now=True)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Replace_Water_Meter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('meter_no', models.CharField(max_length=200)),
                ('reading', models.IntegerField(default=0)),
                ('reason', models.CharField(max_length=200)),
                ('date_updated', models.DateTimeField(auto_now=True)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('profile', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='waterworks.profile')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Reading_Period',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('month', models.CharField(choices=[('1', 'January'), ('2', 'February'), ('3', 'March'), ('4', 'April'), ('5', 'May'), ('6', 'June'), ('7', 'July'), ('8', 'August'), ('9', 'September'), ('10', 'October'), ('11', 'November'), ('12', 'December')], default=1, max_length=200)),
                ('due_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('disconnection_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('date_updated', models.DateTimeField(auto_now=True)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('year', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='waterworks.year')),
            ],
        ),
        migrations.CreateModel(
            name='Reading',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('previous_reading', models.IntegerField(default=0)),
                ('previous_reading_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('present_reading', models.IntegerField(default=0)),
                ('present_reading_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('amount', models.DecimalField(decimal_places=2, default=0, max_digits=50)),
                ('service_charge', models.DecimalField(decimal_places=2, default=0, max_digits=50)),
                ('water_meter_charge', models.DecimalField(decimal_places=2, default=0, max_digits=50)),
                ('date_updated', models.DateTimeField(auto_now=True)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='waterworks.profile')),
                ('reading_period', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='waterworks.reading_period')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Permanently_Disconnected',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('remarks', models.CharField(max_length=200)),
                ('date_updated', models.DateTimeField(auto_now=True)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('profile', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='waterworks.profile')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Modification_Charges',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('action', models.CharField(choices=[('1', 'Added'), ('2', 'Deducted')], default=1, max_length=200)),
                ('charges_type', models.CharField(choices=[('1', 'Service Charge'), ('2', 'Water Meter Charge')], default=1, max_length=200)),
                ('amount', models.DecimalField(decimal_places=2, default=0, max_digits=50)),
                ('remarks', models.CharField(max_length=200)),
                ('date_updated', models.DateTimeField(auto_now=True)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='waterworks.profile')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Meter_Installation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('meter_no', models.CharField(max_length=200)),
                ('reading', models.IntegerField(default=0)),
                ('status', models.CharField(choices=[('1', 'Active'), ('2', 'Disconnected')], default=1, max_length=200)),
                ('date_reading', models.DateTimeField(default=django.utils.timezone.now)),
                ('date_updated', models.DateTimeField(auto_now=True)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('profile', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='waterworks.profile')),
                ('reading_period', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='waterworks.reading_period')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Collection_Charges_Cancelled',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mode_of_payment', models.CharField(choices=[('1', 'Cash'), ('2', 'Check')], default=1, max_length=200)),
                ('charges_type_collection', models.CharField(choices=[('1', 'Service Charge'), ('2', 'Water Meter Charge'), ('3', 'Reconnection')], default=1, max_length=200)),
                ('or_number', models.CharField(max_length=200)),
                ('amount', models.DecimalField(decimal_places=2, default=0, max_digits=50)),
                ('reason', models.CharField(max_length=200)),
                ('date_updated', models.DateTimeField(auto_now=True)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='waterworks.profile')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Collection_Charges',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mode_of_payment', models.CharField(choices=[('1', 'Cash'), ('2', 'Check')], default=1, max_length=200)),
                ('charges_type_collection', models.CharField(choices=[('1', 'Service Charge'), ('2', 'Water Meter Charge'), ('3', 'Reconnection')], default=1, max_length=200)),
                ('or_number', models.CharField(max_length=200)),
                ('amount', models.DecimalField(decimal_places=2, default=0, max_digits=50)),
                ('date_updated', models.DateTimeField(auto_now=True)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='waterworks.profile')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Classification_Rates',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('rate', models.IntegerField(default=0)),
                ('value_expression', models.IntegerField(default=0)),
                ('date_updated', models.DateTimeField(auto_now=True)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('classification', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='waterworks.classification')),
            ],
        ),
        migrations.CreateModel(
            name='Activity_Logs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('logs', models.CharField(choices=[('1', 'Account added'), ('2', 'Information Changed'), ('3', 'Intalled Water Meter'), ('4', 'Change Info Water Meter'), ('5', 'Replace Water Meter')], default=1, max_length=200)),
                ('date_updated', models.DateTimeField(auto_now=True)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='waterworks.profile')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
