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
from waterworks.models import Profile,Barangay
success = 'success'
info = 'info'
error = 'error'
warning = 'warning'
question = 'question'

class Waterworks_Reading(LoginRequiredMixin,TemplateView):
    template_name = 'waterworks/pages/reading.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['barangay'] = Barangay.objects.filter(is_active=True)
        return context

class Waterworks_Reading_Table_AJAXView(LoginRequiredMixin,View):
    queryset = Profile.objects.all()
    template_name = 'waterworks/tables/reading_table.html'
    def get(self, request):
        data = dict()
        try:
            search = self.request.GET.get('search')
            barangay = self.request.GET.get('barangay')
            start = self.request.GET.get('start')
            end = self.request.GET.get('end')
        except KeyError:
            search = None
            start = None
            end = None
        if barangay or search or start or end:
            data['form_is_valid'] = True
            data['counter'] = self.queryset.filter(Q(firstname__icontains = search)|Q(surname__icontains=search),meter_installation__status=1,barangay=barangay).count()
            profile = self.queryset.filter(Q(firstname__icontains = search)|Q(surname__icontains=search),meter_installation__status=1,barangay=barangay).order_by('surname','firstname')[int(start):int(end)]
            data['profile'] = render_to_string(self.template_name,{'profile':profile,'start':start})
        return JsonResponse(data)
