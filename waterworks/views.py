from django.shortcuts import render,redirect,get_object_or_404
from django.views.generic import (
    View,
    TemplateView,
    ListView,
    DetailView,
)

#functions
from django.db.models.functions import Coalesce,Concat
from django.db.models import Q,F,Sum,Count
from django.db.models import Value
from django.urls import reverse
#datetime
from datetime import datetime
#JSON AJAX
from django.template.loader import render_to_string
from django.template import RequestContext
from django.contrib.auth.mixins import LoginRequiredMixin
from .decorators import ConfigurationRequired
from .models import (
    Profile,
    Meter_Installation,
    Reading,
    Reading_Period,
    Permanently_Disconnected,
)

class Waterworks_Home(LoginRequiredMixin,ConfigurationRequired,TemplateView):
    template_name = 'waterworks/pages/dashboard.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        reading_period = Reading_Period.objects.latest('pk')
        counter = Profile.objects.filter(meter_installation__status=1,meter_installation__reading_period__lt=reading_period).count()
        if counter > 0:
            context['status'] = True
            context['counter'] = str(counter)
        context['total_profile'] = Profile.objects.all().count()
        profile_new = Profile.objects.exclude(id__in = Meter_Installation.objects.values('profile_id'))
        context['total_new'] = profile_new.exclude(id__in = Permanently_Disconnected.objects.values('profile_id')).count()
        context['monthly_consumption'] = Reading.objects.filter(reading_period=reading_period).values('reading_period').annotate(dsum=Sum(F('present_reading')-F('previous_reading')))[0]['dsum']
        context['yearly_consumption'] = Reading.objects.filter(reading_period__year=reading_period.year).values('reading_period__year').annotate(dsum=Sum(F('present_reading')-F('previous_reading')))[0]['dsum']
        context['classification_name_list'] = Profile.objects.filter(meter_installation__status__in = [1,2]).values('classification__name').order_by('classification__name').annotate(counter=Count('classification__name'))
        context['barangay_name_list'] = Profile.objects.filter(meter_installation__status__in = [1,2]).values('barangay__name').order_by('barangay__name').annotate(counter=Count('barangay__name'))
        return context

class Waterworks_Accounts(LoginRequiredMixin,TemplateView):
    template_name = 'waterworks/pages/accounts.html'
