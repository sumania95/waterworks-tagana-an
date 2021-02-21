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
from waterworks.models import Reading
success = 'success'
info = 'info'
error = 'error'
warning = 'warning'
question = 'question'

class Waterworks_Reading(TemplateView):
    template_name = 'waterworks/pages/reading.html'

class Waterworks_Reading_Table_AJAXView(View):
    queryset = Reading.objects.all()
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
        if barangay or search or start or end:
            data['form_is_valid'] = True
            data['counter'] = self.queryset.filter(name__icontains = search).count()
            reading = self.queryset.filter(name__icontains = search).order_by('name')[int(start):int(end)]
            data['reading'] = render_to_string(self.template_name,{'reading':reading,'start':start})
        return JsonResponse(data)
