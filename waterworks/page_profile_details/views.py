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
    Reading,
    Collection_Charges,
    Activity_Logs,
)

success = 'success'
info = 'info'
error = 'error'
warning = 'warning'
question = 'question'
from django.utils import timezone

class Waterworks_Profile_Detail(DetailView):
    model = Profile
    template_name = 'waterworks/pages/profile_detail.html'

class Waterworks_Profile_Detail_Overview_AJAXView(View):
    template_name = 'waterworks/pages/profile_detail_overview.html'
    def get(self, request,pk):
        data = dict()
        context = {
            'pk': pk,
        }
        data['html_form'] = render_to_string(self.template_name,context)
        return JsonResponse(data)

class Waterworks_Profile_Detail_Reading_AJAXView(View):
    template_name = 'waterworks/pages/profile_detail_reading.html'
    def get(self, request,pk):
        data = dict()
        context = {
            'pk': pk,
        }
        data['html_form'] = render_to_string(self.template_name,context)
        return JsonResponse(data)

class Waterworks_Profile_Detail_Reading_Table_AJAXView(View):
    queryset = Reading.objects.all()
    template_name = 'waterworks/tables/profile_detail_reading_table.html'
    def get(self, request,pk):
        data = dict()
        try:
            start = self.request.GET.get('start')
            end = self.request.GET.get('end')
        except KeyError:
            start = None
            end = None
        if start or end:
            data['form_is_valid'] = True
            data['counter'] = self.queryset.filter(profile_id=pk).count()
            barangay = self.queryset.filter(profile_id=pk).order_by('id')[int(start):int(end)]
            data['reading'] = render_to_string(self.template_name,{'reading':barangay,'start':start})
        return JsonResponse(data)

class Waterworks_Profile_Detail_Collection_AJAXView(View):
    template_name = 'waterworks/pages/profile_detail_collection.html'
    def get(self, request,pk):
        data = dict()
        context = {
            'pk': pk,
        }
        data['html_form'] = render_to_string(self.template_name,context)
        return JsonResponse(data)

class Waterworks_Profile_Detail_Collection_Table_AJAXView(View):
    queryset = Collection_Charges.objects.all()
    template_name = 'waterworks/tables/profile_detail_collection_table.html'
    def get(self, request,pk):
        data = dict()
        try:
            start = self.request.GET.get('start')
            end = self.request.GET.get('end')
        except KeyError:
            start = None
            end = None
        if start or end:
            data['form_is_valid'] = True
            data['counter'] = self.queryset.filter(profile_id=pk).count()
            collection = self.queryset.filter(profile_id=pk).order_by('-date_created')[int(start):int(end)]
            data['collection'] = render_to_string(self.template_name,{'collection':collection,'start':start})
        return JsonResponse(data)

class Waterworks_Profile_Detail_Activity_AJAXView(View):
    template_name = 'waterworks/pages/profile_detail_activity.html'
    def get(self, request,pk):
        data = dict()
        context = {
            'pk': pk,
        }
        data['html_form'] = render_to_string(self.template_name,context)
        return JsonResponse(data)

class Waterworks_Profile_Detail_Activity_Table_AJAXView(View):
    queryset = Activity_Logs.objects.all()
    template_name = 'waterworks/tables/profile_detail_activity_table.html'
    def get(self, request,pk):
        data = dict()
        try:
            start = self.request.GET.get('start')
            end = self.request.GET.get('end')
        except KeyError:
            start = None
            end = None
        if start or end:
            data['form_is_valid'] = True
            data['counter'] = self.queryset.filter(profile_id=pk).count()
            activity = self.queryset.filter(profile_id=pk).order_by('-date_created')[int(start):int(end)]
            data['activity'] = render_to_string(self.template_name,{'activity':activity,'start':start})
        return JsonResponse(data)
