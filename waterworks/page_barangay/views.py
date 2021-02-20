from django.shortcuts import render,redirect,get_object_or_404
from django.views.generic import (
    View,
    TemplateView,
    ListView,
    DetailView,
)

#JSON AJAX
from django.template.loader import render_to_string
from django.template import RequestContext
from django.contrib.auth.mixins import LoginRequiredMixin
# Models
from waterworks.models import Barangay

class Waterworks_Barangay_AJAXView(View):
    queryset = Barangay.objects.all()
    template_name = 'waterworks/tables/table_barangay.html'
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
            data['table'] = render_to_string(self.template,{'barangay':barangay})
        return JsonResponse(data)
