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

from waterworks.models import Reports

success = 'success'
info = 'info'
error = 'error'
warning = 'warning'
question = 'question'

class Waterworks_Reports(LoginRequiredMixin,TemplateView):
    template_name = 'waterworks/pages/reports.html'


class Waterworks_Reports_Table_AJAXView(LoginRequiredMixin,View):
    queryset = Reports.objects.all()
    template_name = 'waterworks/tables/reports_table.html'
    def get(self, request):
        data = dict()
        try:
            search = self.request.GET.get('search')
            start = self.request.GET.get('start')
            end = self.request.GET.get('end')
        except KeyError:
            search = None
            start = None
            end = None
        if search or start or end:
            data['form_is_valid'] = True
            data['counter'] = self.queryset.filter(name__icontains = search).count()
            reports = self.queryset.filter(name__icontains = search).order_by('name')[int(start):int(end)]
            data['reports'] = render_to_string(self.template_name,{'reports':reports,'start':start})
        return JsonResponse(data)
