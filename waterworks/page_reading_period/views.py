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
from waterworks.models import Reading_Period,Year
from .forms import Reading_PeriodForm,Reading_Period_UpdateForm
success = 'success'
info = 'info'
error = 'error'
warning = 'warning'
question = 'question'

class Waterworks_Reading_Period(LoginRequiredMixin,TemplateView):
    template_name = 'waterworks/pages/reading_period.html'

class Waterworks_Reading_Period_Create(LoginRequiredMixin,TemplateView):
    template_name = 'waterworks/components/reading_period_create.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "New Reading Period"
        return context

class Waterworks_Reading_Period_Create_AJAXView(LoginRequiredMixin,View):
    template_name = 'waterworks/forms/reading_period_forms.html'
    def get(self, request):
        data = dict()
        form = Reading_PeriodForm()
        context = {
            'form': form,
            'is_Create': True,
            'btn_name': "primary",
            'btn_title': "Submit",
        }
        data['html_form'] = render_to_string(self.template_name,context)
        return JsonResponse(data)
    def post(self, request):
        data =  dict()
        if request.method == 'POST':
            form = Reading_PeriodForm(request.POST,request.FILES)
            year = Year.objects.filter(is_active=True).first()
            if form.is_valid():
                reading_period_exists = Reading_Period.objects.filter(year=year,month=form.instance.month).exists()
                print(form.instance.month)
                if reading_period_exists:
                    data['message_type'] = warning
                    data['message_title'] = 'Duplicated Entry.'
                else:
                    form.instance.year = year
                    form.instance.user = self.request.user
                    reading_period = form.save()
                    data['message_type'] = success
                    data['message_title'] = 'Successfully saved.'
                    data['url'] = reverse('waterworks_reading_period_detail',kwargs={'pk':reading_period.id})
        return JsonResponse(data)

class Waterworks_Reading_Period_Update(LoginRequiredMixin,TemplateView):
    template_name = 'waterworks/components/reading_period_update.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        try:
            id = self.kwargs['pk']
            context['reading_period'] = Reading_Period.objects.get(id = id)
        except Exception as e:
            pass
        context['title'] = "Update Reading Period"
        return context

class Waterworks_Reading_Period_Update_AJAXView(LoginRequiredMixin,View):
    template_name = 'waterworks/forms/reading_period_forms.html'
    def get(self, request):
        data = dict()
        try:
            id = self.request.GET.get('id')
        except KeyError:
            id = None
        reading_period = Reading_Period.objects.get(pk=id)
        form = Reading_Period_UpdateForm(instance=reading_period)
        context = {
            'form': form,
            'reading_period':reading_period,
            'is_Create': False,
            'btn_name': "warning",
            'btn_title': "Update",
        }
        data['html_form'] = render_to_string(self.template_name,context)
        return JsonResponse(data)

class Waterworks_Reading_Period_Update_Save_AJAXView(LoginRequiredMixin,View):
    def post(self, request,pk):
        data = dict()
        reading_period = Reading_Period.objects.get(pk=pk)
        if request.method == 'POST':
            form = Reading_Period_UpdateForm(request.POST,request.FILES,instance=reading_period)
            if form.is_valid():
                form.save()
                data['message_type'] = success
                data['message_title'] = 'Successfully updated.'
        return JsonResponse(data)

class Waterworks_Reading_Period_Table_AJAXView(LoginRequiredMixin,View):
    queryset = Reading_Period.objects.all()
    template_name = 'waterworks/tables/reading_period_table.html'
    def get(self, request):
        data = dict()
        try:
            start = self.request.GET.get('start')
            end = self.request.GET.get('end')
        except KeyError:
            start = None
            end = None
        if start or end:
            year = Year.objects.filter(is_active=True).first()
            data['form_is_valid'] = True
            data['counter'] = self.queryset.filter(year=year).count()
            reading_period = self.queryset.filter(year=year).extra(select={'int_month': 'CAST(month AS INTEGER)'}).order_by('int_month')[int(start):int(end)]
            data['reading_period'] = render_to_string(self.template_name,{'reading_period':reading_period,'start':start})
        return JsonResponse(data)
