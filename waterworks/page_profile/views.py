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
    Reading_Period,
    Meter_Installation,
)
from .forms import (
    ProfileForm,
    Meter_InstallationForm,
)
success = 'success'
info = 'info'
error = 'error'
warning = 'warning'
question = 'question'
from django.utils import timezone

class Waterworks_Profile(TemplateView):
    template_name = 'waterworks/pages/profile.html'

class Waterworks_Profile_Detail(DetailView):
    model = Profile
    template_name = 'waterworks/pages/profile_detail.html'

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
                data['url'] = reverse('waterworks_profile_detail',kwargs={'pk':profile.id})
        return JsonResponse(data)

# meter installation
class Waterworks_Profile_Meter_Installation_Create(TemplateView):
    template_name = 'waterworks/components/meter_installation_create.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Install Water Meter"
        try:
            id = self.kwargs['pk']
            context['profile'] = Profile.objects.get(id = id)
        except Exception as e:
            pass
        return context

class Waterworks_Profile_Meter_Installation_Create_AJAXView(View):
    template_name = 'waterworks/forms/meter_installation_forms.html'
    def get(self, request):
        data = dict()
        try:
            id = self.request.GET.get('id')
        except KeyError:
            id = None
        profile = Profile.objects.get(pk=id)
        form = Meter_InstallationForm()
        context = {
            'form': form,
            'profile': profile,
            'is_Create': True,
            'btn_name': "primary",
            'btn_title': "Submit",
        }
        data['html_form'] = render_to_string(self.template_name,context)
        return JsonResponse(data)

class Waterworks_Profile_Meter_Installation_Create_Save_AJAXView(View):
    def post(self, request,pk):
        data = dict()
        profile = Profile.objects.get(pk=pk)
        reading_period = Reading_Period.objects.last()
        if request.method == 'POST':
            form = Meter_InstallationForm(request.POST,request.FILES)
            if form.is_valid():
                meter_exists = Meter_Installation.objects.filter(meter_no=form.instance.meter_no).exists()
                if meter_exists:
                    data['message_type'] = warning
                    data['message_title'] = 'Duplicated Meter Number.'
                else:
                    form.instance.profile = profile
                    form.instance.reading_period = reading_period
                    form.instance.user = self.request.user
                    form.instance.status = 1
                    form.instance.date_reading = timezone.now()
                    form.save()
                    data['message_type'] = success
                    data['message_title'] = 'Successfully updated.'
                    data['url'] = reverse('waterworks_profile_detail',kwargs={'pk':profile.id})
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
            data['counter'] = self.queryset.filter(Q(firstname__icontains = search)|Q(surname__icontains = search)).count()
            profile = self.queryset.filter(Q(firstname__icontains = search)|Q(surname__icontains = search)).order_by('firstname')[int(start):int(end)]
            data['profile'] = render_to_string(self.template_name,{'profile':profile,'start':start})
        return JsonResponse(data)
