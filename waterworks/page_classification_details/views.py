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
    Classification,
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
    model = Classification
    template_name = 'waterworks/pages/classification_detail.html'

class Waterworks_Classification_Detail_Create_AJAXView(LoginRequiredMixin,View):
    template_name = 'waterworks/forms/classification_rates_forms.html'
    def get(self, request,pk):
        data = dict()
        classification = Classification.objects.get(id=pk)
        form = Classification_RatesForm()
        context = {
            'form': form,
            'classification': classification,
            'title': "New Rates",
            'is_Create': True,
            'btn_name': "primary",
            'btn_title': "Save",
        }
        data['html_form'] = render_to_string(self.template_name,context)
        return JsonResponse(data)
    def post(self, request,pk):
        data =  dict()
        classification = Classification.objects.get(id=pk)
        if request.method == 'POST':
            form = Classification_RatesForm(request.POST,request.FILES)
            if form.is_valid():
                form.instance.classification = classification
                form.save()
                data['message_type'] = success
                data['message_title'] = 'Successfully saved.'
        return JsonResponse(data)

class Waterworks_Classification_Detail_Update_AJAXView(LoginRequiredMixin,View):
    template_name = 'waterworks/forms/classification_rates_forms.html'
    def get(self, request,pk):
        data = dict()
        classification_rates = Classification_Rates.objects.get(id=pk)
        form = Classification_RatesForm(instance=classification_rates)
        context = {
            'form': form,
            'classification_rates': classification_rates,
            'title': "Update Rates",
            'is_Create': False,
            'btn_name': "warning",
            'btn_title': "Update",
        }
        data['html_form'] = render_to_string(self.template_name,context)
        return JsonResponse(data)
    def post(self, request,pk):
        data =  dict()
        classification_rates = Classification_Rates.objects.get(id=pk)
        if request.method == 'POST':
            form = Classification_RatesForm(request.POST,request.FILES,instance=classification_rates)
            if form.is_valid():
                form.save()
                data['message_type'] = success
                data['message_title'] = 'Successfully updated.'
        return JsonResponse(data)

class Waterworks_Classification_Detail_Delete_AJAXView(LoginRequiredMixin,View):
    def post(self, request,pk):
        data =  dict()
        if request.method == 'POST':
            Classification_Rates.objects.get(id=pk).delete()
            data['message_type'] = success
            data['message_title'] = 'Successfully deleted.'
        return JsonResponse(data)

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
