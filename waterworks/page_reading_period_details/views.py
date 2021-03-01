from django.shortcuts import render,redirect,get_object_or_404
from django.views.generic import (
    View,
    TemplateView,
    ListView,
    DetailView,
)
#functions
from django.db.models.functions import Coalesce,Concat
from django.db.models import Q,F,Sum,Count,Max
from django.db.models import Value
from django.urls import reverse

#JSON AJAX
from django.template.loader import render_to_string
from django.http import JsonResponse
from django.template import RequestContext
from django.contrib.auth.mixins import LoginRequiredMixin
# Models
from waterworks.models import (
    Reading_Period,
    Meter_Installation,
    Barangay,
    Profile,
    Settings,
)
from waterworks.render import (
    Render,
)

success = 'success'
info = 'info'
error = 'error'
warning = 'warning'
question = 'question'
from django.utils import timezone

class Waterworks_Reading_Period_Detail(LoginRequiredMixin,DetailView):
    model = Reading_Period
    template_name = 'waterworks/pages/reading_period_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        try:
            id = self.kwargs['pk']
            context['barangay'] = Barangay.objects.filter(is_active=True)
        except Exception as e:
            pass
        return context

class Waterworks_Reading_Period_Print(LoginRequiredMixin,View):
    def get(self, request,pk):
        now = timezone.now()
        try:
            barangay_id = self.request.GET.get('barangay_id')
        except KeyError:
            barangay_id = None
        settings = Settings.objects.first()
        reading_period = Reading_Period.objects.get(id=pk)
        barangay = Barangay.objects.get(id=barangay_id)
        profile = Profile.objects.filter(meter_installation__reading_period__lt=reading_period,meter_installation__status = 1,barangay_id=barangay_id).order_by('meter_installation__cluster','surname','firstname','middlename')
        params = {
            'now': now,
            'reading_period' :reading_period,
            'barangay' :barangay,
            'settings' :settings,
            'profile': profile,
        }
        pdf = Render.render('waterworks/reports/reading_period_print.html', params)
        return pdf
