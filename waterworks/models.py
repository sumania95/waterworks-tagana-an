from django.db import models
from django.db.models import Model, ForeignKey, ManyToManyField
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime
from django.utils import timezone

status = (
    ('1', 'New Application',),
    ('2', 'Active',),
    ('3', 'Disconnected',),
    ('4', 'Permanently Disconnected',),
)

class Waterworks_Profile(models.Model):
    surname         = models.CharField(max_length = 200)
    firstname       = models.CharField(max_length = 200)
    middlename      = models.CharField(max_length = 200,blank=True)
    barangay        = models.CharField(max_length = 200)
    status          = models.CharField(max_length=200,choices=status,default=1)
    meter_no        = models.CharField(max_length = 200,blank=True)
    reading         = models.IntegerField(default=0)
    service_charge  = models.DecimalField(default=0,max_digits = 50,decimal_places=2)
    date_updated    = models.DateTimeField(auto_now = True)
    date_created    = models.DateTimeField(auto_now_add = True)

    @property
    def primary_key_custom(self):
        return str(self.date_created.year) + str(self.id)

    class Meta:
        ordering = ['surname','firstname','middlename']
