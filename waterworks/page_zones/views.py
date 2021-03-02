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
    Profile,
    Barangay,
    Meter_Installation,
)
from .forms import (
    Meter_Installation_Cluster_Form,
    Meter_Installation_Sequence_Form,
)
from django.utils import timezone


success = 'success'
info = 'info'
error = 'error'
warning = 'warning'
question = 'question'

class Waterworks_Zones(LoginRequiredMixin,TemplateView):
    template_name = 'waterworks/pages/zones.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['barangay'] = Barangay.objects.filter(is_active=True)
        return context

class Waterworks_Zones_Table_AJAXView(LoginRequiredMixin,View):
    queryset = Profile.objects.all()
    template_name_cluster = 'waterworks/tables/zones_cluster_table.html'
    template_name_sequence = 'waterworks/tables/zones_sequence_table.html'
    def get(self, request):
        data = dict()
        try:
            search = self.request.GET.get('search')
            barangay = self.request.GET.get('barangay')
            zones = self.request.GET.get('zones')
            start = self.request.GET.get('start')
            end = self.request.GET.get('end')
        except KeyError:
            zones = None
            search = None
            start = None
            end = None
        if barangay or search or start or end:
            data['form_is_valid'] = True
            data['counter'] = self.queryset.filter(Q(firstname__icontains = search)|Q(surname__icontains=search),meter_installation__status__in=[1,2],barangay=barangay).count()
            if zones == 'Cluster':
                profile = self.queryset.filter(Q(firstname__icontains = search)|Q(surname__icontains=search),meter_installation__status__in=[1,2],barangay=barangay).order_by('meter_installation__cluster','surname','firstname')[int(start):int(end)]
                data['profile'] = render_to_string(self.template_name_cluster,{'profile':profile,'start':start})
            elif zones == 'Sequence':
                profile = self.queryset.filter(Q(firstname__icontains = search)|Q(surname__icontains=search),meter_installation__status__in=[1,2],barangay=barangay).order_by('meter_installation__sequence','surname','firstname')[int(start):int(end)]
                data['profile'] = render_to_string(self.template_name_sequence,{'profile':profile,'start':start})
        return JsonResponse(data)

class Waterworks_Zones_Cluster_AJAXView(LoginRequiredMixin,View):
    template_name = 'waterworks/forms/cluster_sequence_forms.html'
    def get(self, request,pk):
        data = dict()
        profile = Meter_Installation.objects.get(profile_id=pk)
        form = Meter_Installation_Cluster_Form(instance=profile)
        context = {
            'form': form,
            'profile': profile,
            'title': "Cluster",
            'is_Cluster': True,
            'btn_name': "warning",
            'btn_title': "Change",
        }
        data['html_form'] = render_to_string(self.template_name,context)
        return JsonResponse(data)
    def post(self, request,pk):
        data =  dict()
        profile = Meter_Installation.objects.get(profile_id=pk)
        if request.method == 'POST':
            form = Meter_Installation_Cluster_Form(request.POST,request.FILES,instance=profile)
            if form.is_valid():
                form.save()
                data['message_type'] = success
                data['message_title'] = 'Successfully changed.'
        return JsonResponse(data)

class Waterworks_Zones_Sequence_AJAXView(LoginRequiredMixin,View):
    template_name = 'waterworks/forms/cluster_sequence_forms.html'
    def get(self, request,pk):
        data = dict()
        profile = Meter_Installation.objects.get(profile_id=pk)
        form = Meter_Installation_Sequence_Form(instance=profile)
        context = {
            'form': form,
            'profile': profile,
            'title': "Sequence",
            'is_Sequence': True,
            'btn_name': "info",
            'btn_title': "Change",
        }
        data['html_form'] = render_to_string(self.template_name,context)
        return JsonResponse(data)
    def post(self, request,pk):
        data =  dict()
        profile = Meter_Installation.objects.get(profile_id=pk)
        if request.method == 'POST':
            form = Meter_Installation_Sequence_Form(request.POST,request.FILES,instance=profile)
            if form.is_valid():
                form.save()
                data['message_type'] = success
                data['message_title'] = 'Successfully changed.'
        return JsonResponse(data)
