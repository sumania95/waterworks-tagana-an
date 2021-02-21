from django.shortcuts import render,redirect,get_object_or_404
from django.views.generic import (
    View,
    TemplateView,
    ListView,
    DetailView,
)

#JSON AJAX
from django.template.loader import render_to_string
from django.http import JsonResponse
from django.template import RequestContext
from django.contrib.auth.mixins import LoginRequiredMixin
# Models
from waterworks.models import Barangay
from .forms import BarangayForm
success = 'success'
info = 'info'
error = 'error'
warning = 'warning'
question = 'question'

class Waterworks_Barangay(TemplateView):
    template_name = 'waterworks/pages/barangay.html'

class Waterworks_Barangay_Create(TemplateView):
    template_name = 'waterworks/components/barangay_create.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "New Barangay"
        return context

class Waterworks_Barangay_Create_AJAXView(View):
    template_name = 'waterworks/forms/barangay_forms.html'
    def get(self, request):
        data = dict()
        form = BarangayForm()
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
            form = BarangayForm(request.POST,request.FILES)
            if form.is_valid():
                form.save()
                data['message_type'] = success
                data['message_title'] = 'Successfully saved.'
        return JsonResponse(data)

class Waterworks_Barangay_Update(TemplateView):
    template_name = 'waterworks/components/barangay_update.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        try:
            id = self.kwargs['pk']
            context['barangay'] = Barangay.objects.get(id = id)
        except Exception as e:
            pass
        context['title'] = "Update Barangay"
        return context

class Waterworks_Barangay_Update_AJAXView(View):
    template_name = 'waterworks/forms/barangay_forms.html'
    def get(self, request):
        data = dict()
        try:
            id = self.request.GET.get('id')
        except KeyError:
            id = None
        barangay = Barangay.objects.get(pk=id)
        form = BarangayForm(instance=barangay)
        context = {
            'form': form,
            'barangay':barangay,
            'is_Create': False,
            'btn_name': "warning",
            'btn_title': "Update",
        }
        data['html_form'] = render_to_string(self.template_name,context)
        return JsonResponse(data)

class Waterworks_Barangay_Update_Save_AJAXView(View):
    def post(self, request,pk):
        data = dict()
        barangay = Barangay.objects.get(pk=pk)
        if request.method == 'POST':
            form = BarangayForm(request.POST,request.FILES,instance=barangay)
            if form.is_valid():
                form.save()
                data['message_type'] = success
                data['message_title'] = 'Successfully updated.'
        return JsonResponse(data)

class Waterworks_Barangay_Table_AJAXView(View):
    queryset = Barangay.objects.all()
    template_name = 'waterworks/tables/barangay_table.html'
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
            barangay = self.queryset.filter(name__icontains = search).order_by('name')[int(start):int(end)]
            data['barangay'] = render_to_string(self.template_name,{'barangay':barangay,'start':start})
        return JsonResponse(data)
