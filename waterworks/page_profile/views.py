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
from waterworks.models import Profile
from .forms import ProfileForm
success = 'success'
info = 'info'
error = 'error'
warning = 'warning'
question = 'question'

class Waterworks_Profile(TemplateView):
    template_name = 'waterworks/pages/profile.html'

class Waterworks_Profile_Create(TemplateView):
    template_name = 'waterworks/components/profile_create.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "New Profile"
        return context

class Waterworks_Profile_Create_AJAXView(View):
    template_name = 'waterworks/forms/profile_forms.html'
    def get(self, request):
        data = dict()
        form = ProfileForm()
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
            form = ProfileForm(request.POST,request.FILES)
            if form.is_valid():
                form.save()
                data['message_type'] = success
                data['message_title'] = 'Successfully saved.'
        return JsonResponse(data)

class Waterworks_Profile_Update(TemplateView):
    template_name = 'waterworks/components/profile_update.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        try:
            id = self.kwargs['pk']
            context['profile'] = Profile.objects.get(id = id)
        except Exception as e:
            pass
        context['title'] = "Update Profile"
        return context

class Waterworks_Profile_Update_AJAXView(View):
    template_name = 'waterworks/forms/profile_forms.html'
    def get(self, request):
        data = dict()
        try:
            id = self.request.GET.get('id')
        except KeyError:
            id = None
        profile = Profile.objects.get(pk=id)
        form = ProfileForm(instance=profile)
        context = {
            'form': form,
            'profile':profile,
            'is_Create': False,
            'btn_name': "warning",
            'btn_title': "Update",
        }
        data['html_form'] = render_to_string(self.template_name,context)
        return JsonResponse(data)

class Waterworks_Profile_Update_Save_AJAXView(View):
    def post(self, request,pk):
        data = dict()
        profile = Profile.objects.get(pk=pk)
        if request.method == 'POST':
            form = ProfileForm(request.POST,request.FILES,instance=profile)
            if form.is_valid():
                form.save()
                data['message_type'] = success
                data['message_title'] = 'Successfully updated.'
        return JsonResponse(data)

class Waterworks_Profile_Table_AJAXView(View):
    queryset = Profile.objects.all()
    template_name = 'waterworks/tables/profile_table.html'
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
            data['counter'] = self.queryset.filter(firstname__icontains = search).count()
            profile = self.queryset.filter(firstname__icontains = search).order_by('firstname')[int(start):int(end)]
            data['profile'] = render_to_string(self.template_name,{'profile':profile,'start':start})
        return JsonResponse(data)
