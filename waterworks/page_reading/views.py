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
    Barangay,
    Meter_Installation,
    Reading_Period,
    Classification,
    Classification_Rates,
)
from .forms import ReadingForm
from django.utils import timezone


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
        form = ReadingForm()
        if barangay or search or start or end:
            data['form_is_valid'] = True
            reading_period = Reading_Period.objects.latest('pk')
            data['counter'] = self.queryset.filter(Q(firstname__icontains = search)|Q(surname__icontains=search),meter_installation__status=1,barangay=barangay,meter_installation__reading_period__lt=reading_period).count()
            profile = self.queryset.filter(Q(firstname__icontains = search)|Q(surname__icontains=search),meter_installation__status=1,barangay=barangay,meter_installation__reading_period__lt = reading_period).order_by('surname','firstname')[int(start):int(end)]
            data['profile'] = render_to_string(self.template_name,{'profile':profile,'start':start,'form':form})
        return JsonResponse(data)

class Waterworks_Reading_Create_Save_AJAXView(LoginRequiredMixin,View):
    def post(self, request,pk):
        data =  dict()
        if request.method == 'POST':
            form = ReadingForm(request.POST,request.FILES)
            if form.is_valid():
                present_reading = form.instance.present_reading
                profile = Profile.objects.get(id=pk)
                classification = Classification.objects.get(id=profile.classification_id)
                classification_rates = Classification_Rates.objects.filter(classification=classification).order_by('rate')
                meter_installation = Meter_Installation.objects.get(profile=profile)
                reading_period = Reading_Period.objects.latest('pk')
                total_reading = float(present_reading) - meter_installation.reading
                amount = 0
                if total_reading < 0:
                    data['message_type'] = error
                    data['message_title'] = 'Negative reading.'
                    return JsonResponse(data)
                for p in classification_rates:
                    if float(total_reading) >= p.consumption and p.minimum==True:
                        amount = (float(total_reading) * float(p.blocking_rate)) + float(p.value_expression)
                    elif float(total_reading) >= p.consumption and p.minimum==False:
                        amount = (float(total_reading) * float(p.blocking_rate)) - float(p.value_expression)
                form.instance.user = self.request.user
                form.instance.profile = profile
                form.instance.reading_period = reading_period
                form.instance.previous_reading = meter_installation.reading
                form.instance.previous_reading_date = meter_installation.date_reading
                form.instance.amount = amount
                form.instance.service_charge = profile.service_charge
                form.instance.water_meter_charge = profile.water_meter_charge
                Meter_Installation.objects.filter(profile=profile).update(reading=present_reading,date_reading=timezone.now(),reading_period=reading_period)
                Profile.objects.filter(id=pk).update(service_charge=F('service_charge')+amount,water_meter_charge=F('water_meter_charge')+form.instance.water_meter_charge)
                form.save()
                data['message_type'] = success
                data['message_title'] = 'Successfully saved. ' + str(amount)
        return JsonResponse(data)
