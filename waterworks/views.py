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
    Reading_Period,
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
        return context

class Waterworks_Accounts(LoginRequiredMixin,TemplateView):
    template_name = 'waterworks/pages/accounts.html'
