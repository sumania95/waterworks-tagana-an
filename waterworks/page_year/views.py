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
from waterworks.models import Year
from .forms import YearForm
success = 'success'
info = 'info'
error = 'error'
warning = 'warning'
question = 'question'

class Waterworks_Year(TemplateView):
    template_name = 'waterworks/pages/year.html'

class Waterworks_Year_Create(TemplateView):
    template_name = 'waterworks/components/year_create.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "New Year"
        return context

class Waterworks_Year_Create_AJAXView(View):
    template_name = 'waterworks/forms/year_forms.html'
    def get(self, request):
        data = dict()
        form = YearForm()
        context = {
            'form': form,
            'is_Create': True,
            'btn_name': "primary",
            'btn_title': "Save",
        }
        data['html_form'] = render_to_string(self.template_name,context)
        return JsonResponse(data)
    def post(self, request):
        data =  dict()
        if request.method == 'POST':
            form = YearForm(request.POST,request.FILES)
            if form.is_valid():
                Year.objects.update(is_active=False)
                form.save()
                data['message_type'] = success
                data['message_title'] = 'Successfully saved.'
                data['url'] = reverse('waterworks_year')
        return JsonResponse(data)

class Waterworks_Year_Activate_AJAXView(View):
    def post(self, request,pk):
        data = dict()
        try:
            Year.objects.update(is_active=False)
            Year.objects.filter(id=pk).update(is_active=True)
            data['message_type'] = success
            data['message_title'] = 'Successfully activated.'
        except Exception as e:
            pass
        return JsonResponse(data)

class Waterworks_Year_Table_AJAXView(View):
    queryset = Year.objects.all()
    template_name = 'waterworks/tables/year_table.html'
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
            year = self.queryset.filter(name__icontains = search).order_by('name')[int(start):int(end)]
            data['year'] = render_to_string(self.template_name,{'year':year,'start':start})
        return JsonResponse(data)
