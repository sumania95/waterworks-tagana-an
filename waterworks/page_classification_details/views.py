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
    Classification_Rates,
)
from .forms import (
    Classification_RatesForm,
)

success = 'success'
info = 'info'
error = 'error'
warning = 'warning'
question = 'question'
from django.utils import timezone

class Waterworks_Classification_Detail(LoginRequiredMixin,DetailView):
    model = Classification_Rates
    template_name = 'waterworks/pages/classification_detail.html'

class Waterworks_Classification_Detail_Table_AJAXView(LoginRequiredMixin,View):
    queryset = Classification_Rates.objects.all()
    template_name = 'waterworks/tables/classification_detail_table.html'
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
            data['counter'] = self.queryset.filter(classification_id = pk).count()
            classification = self.queryset.filter(classification_id = pk).order_by('consumption')[int(start):int(end)]
            data['classification'] = render_to_string(self.template_name,{'classification':classification,'start':start})
        return JsonResponse(data)
