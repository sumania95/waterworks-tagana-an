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
from waterworks.models import Classification
from .forms import ClassificationForm
success = 'success'
info = 'info'
error = 'error'
warning = 'warning'
question = 'question'

class Waterworks_Classification(LoginRequiredMixin,TemplateView):
    template_name = 'waterworks/pages/classification.html'

class Waterworks_Classification_Create(LoginRequiredMixin,TemplateView):
    template_name = 'waterworks/components/classification_create.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "New Classification"
        return context

class Waterworks_Classification_Create_AJAXView(LoginRequiredMixin,View):
    template_name = 'waterworks/forms/classification_forms.html'
    def get(self, request):
        data = dict()
        form = ClassificationForm()
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
            form = ClassificationForm(request.POST,request.FILES)
            if form.is_valid():
                form.save()
                data['message_type'] = success
                data['message_title'] = 'Successfully saved.'
        return JsonResponse(data)

class Waterworks_Classification_Update(LoginRequiredMixin,TemplateView):
    template_name = 'waterworks/components/classification_update.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        try:
            id = self.kwargs['pk']
            context['classification'] = Classification.objects.get(id = id)
        except Exception as e:
            pass
        context['title'] = "Update Classification"
        return context

class Waterworks_Classification_Update_AJAXView(LoginRequiredMixin,View):
    template_name = 'waterworks/forms/classification_forms.html'
    def get(self, request):
        data = dict()
        try:
            id = self.request.GET.get('id')
        except KeyError:
            id = None
        classification = Classification.objects.get(pk=id)
        form = ClassificationForm(instance=classification)
        context = {
            'form': form,
            'classification':classification,
            'is_Create': False,
            'btn_name': "warning",
            'btn_title': "Update",
        }
        data['html_form'] = render_to_string(self.template_name,context)
        return JsonResponse(data)

class Waterworks_Classification_Update_Save_AJAXView(LoginRequiredMixin,View):
    def post(self, request,pk):
        data = dict()
        classification = Classification.objects.get(pk=pk)
        if request.method == 'POST':
            form = ClassificationForm(request.POST,request.FILES,instance=classification)
            if form.is_valid():
                form.save()
                data['message_type'] = success
                data['message_title'] = 'Successfully updated.'
        return JsonResponse(data)

class Waterworks_Classification_Delete_AJAXView(LoginRequiredMixin,View):
    def post(self, request,pk):
        data = dict()
        if request.method == 'POST':
            Classification.objects.get(pk=pk).delete()
            data['message_type'] = success
            data['message_title'] = 'Successfully deleted.'
        return JsonResponse(data)

class Waterworks_Classification_Table_AJAXView(LoginRequiredMixin,View):
    queryset = Classification.objects.all()
    template_name = 'waterworks/tables/classification_table.html'
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
            classification = self.queryset.filter(name__icontains = search).order_by('name')[int(start):int(end)]
            data['classification'] = render_to_string(self.template_name,{'classification':classification,'start':start})
        return JsonResponse(data)
