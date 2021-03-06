from django.db import models
from django.db.models import Model, ForeignKey, ManyToManyField
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime
from django.utils import timezone

class Reports(models.Model):
    name                    = models.CharField(max_length = 200)
    url_report              = models.CharField(max_length = 200)
    date_updated            = models.DateTimeField(auto_now = True)
    date_created            = models.DateTimeField(auto_now_add = True)

class Settings(models.Model):
    name                                = models.CharField(max_length = 200)
    address                             = models.CharField(max_length = 200)
    notices                             = models.CharField(default="",max_length = 1000)
    logo                                = models.FileField(upload_to='logo/')
    water_meter_charge                  = models.DecimalField(default=0,max_digits = 50,decimal_places=2)
    disconnection_charge                = models.DecimalField(default=0,max_digits = 50,decimal_places=2)
    permanently_disconnected_charge     = models.DecimalField(default=0,max_digits = 50,decimal_places=2)
    date_updated                        = models.DateTimeField(auto_now = True)
    date_created                        = models.DateTimeField(auto_now_add = True)

class Modem(models.Model):
    ip_address                          = models.CharField(max_length = 200)
    username                            = models.CharField(max_length = 200)
    password                            = models.CharField(max_length = 200)
    date_updated                        = models.DateTimeField(auto_now = True)
    date_created                        = models.DateTimeField(auto_now_add = True)

class Billing_Template(models.Model):
    name                                = models.CharField(max_length = 200)
    file                                = models.FileField(upload_to='template/')
    date_updated                        = models.DateTimeField(auto_now = True)
    date_created                        = models.DateTimeField(auto_now_add = True)

class Account(models.Model):
    user                    = models.OneToOneField(User, on_delete = models.CASCADE)
    surname                 = models.CharField(max_length = 200)
    firstname               = models.CharField(max_length = 200)
    middlename              = models.CharField(max_length = 200,blank=True)
    is_admin                = models.BooleanField(default=False)
    is_waterworks_clerk     = models.BooleanField(default=False)
    is_collection_clerk     = models.BooleanField(default=False)
    date_updated            = models.DateTimeField(auto_now = True)
    date_created            = models.DateTimeField(auto_now_add = True)

    @property
    def name(self):
        return str(self.surname) + ", " + str(self.firstname)

class Barangay(models.Model):
    name                    = models.CharField(max_length = 200)
    is_active               = models.BooleanField(default = True)
    date_updated            = models.DateTimeField(auto_now = True)
    date_created            = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return str(self.name)

    class Meta:
        ordering = ['name']

class Year(models.Model):
    name                    = models.CharField(max_length = 200)
    is_active               = models.BooleanField(default = True)
    date_updated            = models.DateTimeField(auto_now = True)
    date_created            = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return str(self.name)

class Classification(models.Model):
    name                    = models.CharField(max_length = 200)
    date_updated            = models.DateTimeField(auto_now = True)
    date_created            = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return str(self.name)

    class Meta:
        ordering = ['name']

class Classification_Rates(models.Model):
    classification          = models.ForeignKey(Classification, on_delete = models.CASCADE)
    consumption             = models.IntegerField(default = 0)
    blocking_rate           = models.DecimalField(default=0,max_digits = 50,decimal_places=2)
    value_expression        = models.DecimalField(default=0,max_digits = 50,decimal_places=2)
    minimum                 = models.BooleanField(default=False)
    date_updated            = models.DateTimeField(auto_now = True)
    date_created            = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return str(self.classification)+" "+str(self.consumption)

class Profile(models.Model):
    surname                 = models.CharField(max_length = 200)
    firstname               = models.CharField(max_length = 200)
    middlename              = models.CharField(max_length = 200,blank=True)
    barangay                = models.ForeignKey(Barangay, on_delete = models.CASCADE)
    classification          = models.ForeignKey(Classification, on_delete = models.CASCADE)
    service_charge          = models.DecimalField(default=0,max_digits = 50,decimal_places=2)
    water_meter_charge      = models.DecimalField(default=0,max_digits = 50,decimal_places=2)
    reconnection_charge     = models.DecimalField(default=0,max_digits = 50,decimal_places=2)
    date_updated            = models.DateTimeField(auto_now = True)
    date_created            = models.DateTimeField(auto_now_add = True)

    @property
    def primary_key_custom(self):
        return str(self.date_created.year) + str(self.id)

    @property
    def name(self):
        return str(self.surname) + ", " + str(self.firstname)

    class Meta:
        ordering = ['surname','firstname','middlename']

month = (
    ('1', 'January',),
    ('2', 'February',),
    ('3', 'March',),
    ('4', 'April',),
    ('5', 'May',),
    ('6', 'June',),
    ('7', 'July',),
    ('8', 'August',),
    ('9', 'September',),
    ('10', 'October',),
    ('11', 'November',),
    ('12', 'December',),
)

class Reading_Period(models.Model):
    user                    = models.ForeignKey(User, on_delete = models.CASCADE)
    month                   = models.CharField(max_length=200,choices=month)
    year                    = models.ForeignKey(Year, on_delete = models.CASCADE)
    due_date                = models.DateTimeField(default=timezone.now)
    disconnection_date      = models.DateTimeField(default=timezone.now)
    date_updated            = models.DateTimeField(auto_now = True)
    date_created            = models.DateTimeField(auto_now_add = True)

    @property
    def description(self):
        return str(self.month) + " " + str(self.year)

    class Meta:
        ordering = ['month']

logs = (
    ('1', 'Information Changed',),
    ('2', 'Intalled Water Meter',),
    ('3', 'Replace Water Meter',),
    ('4', 'Disconnected',),
    ('5', 'Condemn',),
    ('6', 'Active Meter',),
)

class Activity_Logs(models.Model):
    user                    = models.ForeignKey(User, on_delete = models.CASCADE)
    profile                 = models.ForeignKey(Profile, on_delete = models.CASCADE)
    logs                    = models.CharField(max_length=200,choices=logs,default=1)
    date_updated            = models.DateTimeField(auto_now = True)
    date_created            = models.DateTimeField(auto_now_add = True)

class User_Logs(models.Model):
    user                    = models.ForeignKey(User, on_delete = models.CASCADE)
    user_logs               = models.CharField(max_length=200,choices=logs,default=1)
    date_updated            = models.DateTimeField(auto_now = True)
    date_created            = models.DateTimeField(auto_now_add = True)

status = (
    ('1', 'Active',),
    ('2', 'Disconnected',),
    ('3', 'Permanently Disconnected',),
)

class Meter_Installation(models.Model):
    user                    = models.ForeignKey(User, on_delete = models.CASCADE)
    reading_period          = models.ForeignKey(Reading_Period, on_delete = models.CASCADE)
    profile                 = models.OneToOneField(Profile, on_delete = models.CASCADE)
    meter_no                = models.CharField(max_length = 200)
    reading                 = models.IntegerField(default=0)
    status                  = models.CharField(max_length=200,choices=status)
    cluster                 = models.CharField(default="0000",max_length = 200)
    sequence                = models.CharField(default="0000",max_length = 200)
    date_reading            = models.DateTimeField()
    date_updated            = models.DateTimeField(auto_now = True)
    date_created            = models.DateTimeField(auto_now_add = True)

class Meter_Status_History(models.Model):
    user                    = models.ForeignKey(User, on_delete=models.CASCADE)
    profile                 = models.ForeignKey(Profile, on_delete = models.CASCADE)
    log                     = models.OneToOneField(Activity_Logs, on_delete = models.CASCADE)
    status                  = models.CharField(max_length=200,choices=status)
    reason                  = models.CharField(max_length = 200)
    date_updated            = models.DateTimeField(auto_now = True)
    date_created            = models.DateTimeField(auto_now_add = True)

class Meter_Replace(models.Model):
    user                    = models.ForeignKey(User, on_delete=models.CASCADE)
    profile                 = models.ForeignKey(Profile, on_delete = models.CASCADE)
    old_meter_no            = models.CharField(max_length = 200,blank=True)
    old_reading             = models.IntegerField(default=0)
    meter_no                = models.CharField(max_length = 200)
    reading                 = models.IntegerField(default=0)
    reason                  = models.CharField(max_length = 200)
    date_updated            = models.DateTimeField(auto_now = True)
    date_created            = models.DateTimeField(auto_now_add = True)

class Reading(models.Model):
    user                    = models.ForeignKey(User, on_delete=models.CASCADE)
    profile                 = models.ForeignKey(Profile, on_delete=models.CASCADE)
    reading_period          = models.ForeignKey(Reading_Period, on_delete=models.CASCADE)
    previous_reading        = models.IntegerField(default=0)
    previous_reading_date   = models.DateTimeField()
    present_reading         = models.IntegerField(default=0)
    present_reading_date    = models.DateTimeField(default=timezone.now)
    amount                  = models.DecimalField(default=0,max_digits = 50,decimal_places=2)
    service_charge          = models.DecimalField(default=0,max_digits = 50,decimal_places=2)
    water_meter_charge      = models.DecimalField(default=0,max_digits = 50,decimal_places=2)
    date_updated            = models.DateTimeField(auto_now = True)
    date_created            = models.DateTimeField(auto_now_add = True)

    @property
    def consumption(self):
        return int(self.present_reading) - int(self.previous_reading)
    @property
    def total_amount(self):
        return float(self.amount) + float(self.service_charge)

class Permanently_Disconnected(models.Model):
    user                    = models.ForeignKey(User, on_delete=models.CASCADE)
    profile                 = models.OneToOneField(Profile, on_delete = models.CASCADE)
    remarks                 = models.CharField(max_length = 200)
    date_updated            = models.DateTimeField(auto_now = True)
    date_created            = models.DateTimeField(auto_now_add = True)

action = (
    ('1', 'Added',),
    ('2', 'Deducted',),
)

charges_type = (
    ('1', 'Service Charge',),
    ('2', 'Water Meter Charge',),
)

class Modification_Charges(models.Model):
    user                    = models.ForeignKey(User, on_delete = models.CASCADE)
    profile                 = models.ForeignKey(Profile, on_delete = models.CASCADE)
    action                  = models.CharField(max_length=200,choices=action,default=1)
    charges_type            = models.CharField(max_length=200,choices=charges_type,default=1)
    amount                  = models.DecimalField(default=0,max_digits = 50,decimal_places=2)
    remarks                 = models.CharField(max_length = 200)
    date_updated            = models.DateTimeField(auto_now = True)
    date_created            = models.DateTimeField(auto_now_add = True)

mode_of_payment = (
    ('1', 'Cash',),
    ('2', 'Check',),
)

charges_type_collection = (
    ('1', 'Service Charge',),
    ('2', 'Water Meter Charge',),
    ('3', 'Reconnection',),
)

class Collection_Charges(models.Model):
    user                    = models.ForeignKey(User, on_delete = models.CASCADE)
    profile                 = models.ForeignKey(Profile, on_delete = models.CASCADE)
    mode_of_payment         = models.CharField(max_length=200,choices=mode_of_payment,default=1)
    charges_type_collection = models.CharField(max_length=200,choices=charges_type_collection,default=1)
    or_number               = models.CharField(max_length = 200)
    amount                  = models.DecimalField(default=0,max_digits = 50,decimal_places=2)
    date_updated            = models.DateTimeField(auto_now = True)
    date_created            = models.DateTimeField(auto_now_add = True)

class Collection_Charges_Cancelled(models.Model):
    user                    = models.ForeignKey(User, on_delete = models.CASCADE)
    profile                 = models.ForeignKey(Profile, on_delete = models.CASCADE)
    mode_of_payment         = models.CharField(max_length=200,choices=mode_of_payment,default=1)
    charges_type_collection = models.CharField(max_length=200,choices=charges_type_collection,default=1)
    or_number               = models.CharField(max_length = 200)
    amount                  = models.DecimalField(default=0,max_digits = 50,decimal_places=2)
    reason                  = models.CharField(max_length = 200)
    date_updated            = models.DateTimeField(auto_now = True)
    date_created            = models.DateTimeField(auto_now_add = True)
