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

from waterworks.models import (
    Settings,
    Modem
)
from .forms import (
    SettingsForm,
    ModemForm,
)
success = 'success'
info = 'info'
error = 'error'
warning = 'warning'
question = 'question'

class Waterworks_Settings(LoginRequiredMixin,TemplateView):
    template_name = 'waterworks/pages/settings.html'


class Waterwork_Settings_AJAXView(LoginRequiredMixin,View):
    def get(self, request):
        data = dict()
        setting = Settings.objects.first()
        if setting:
            form = SettingsForm(instance=setting)
        else:
            form = SettingsForm()
        context = {
            'form':form,
            'title' : "Maintenance",
            'btn_name' : 'primary',
            'btn_title' : 'Change',
        }
        data['html_form'] = render_to_string('waterworks/forms/settings_forms.html',context)
        return JsonResponse(data)
    def post(self, request):
        data = dict()
        if request.method == 'POST':
            setting = Settings.objects.first()
            if setting:
                form = SettingsForm(request.POST,request.FILES,instance = setting)
            else:
                form = SettingsForm(request.POST,request.FILES)
            if form.is_valid():
                form.save()
                data['message_type'] = success
                data['message_title'] = 'Successfully changed.'
                data['form_is_valid'] = True
        return JsonResponse(data)

class Waterwork_Modem_AJAXView(LoginRequiredMixin,View):
    def get(self, request):
        data = dict()
        setting = Modem.objects.first()
        if setting:
            form = ModemForm(instance=setting)
        else:
            form = ModemForm()
        context = {
            'form':form,
            'title' : "SMS Modem Configuration",
            'btn_name' : 'primary',
            'btn_title' : 'Change',
        }
        data['html_form'] = render_to_string('waterworks/forms/modem_forms.html',context)
        return JsonResponse(data)
    def post(self, request):
        data = dict()
        if request.method == 'POST':
            setting = Modem.objects.first()
            if setting:
                form = ModemForm(request.POST,request.FILES,instance = setting)
            else:
                form = ModemForm(request.POST,request.FILES)
            if form.is_valid():
                form.save()
                data['message_type'] = success
                data['message_title'] = 'Successfully changed.'
                data['form_is_valid'] = True
        return JsonResponse(data)
