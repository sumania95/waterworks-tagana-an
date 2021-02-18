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
    template_name = 'waterworks/tables/barangay.html'
    def get(self, request):
        data = dict()
        try:
            search = self.request.GET.get('search')
            filter = self.request.GET.get('filter')
        except KeyError:
            search = None
            filter = None
        if search or filter:
            data['form_is_valid'] = True
            data['counter'] = self.queryset.filter(name__icontains = search).count()
            profile = self.queryset.filter(name__icontains = search).order_by('surname','firstname')[:int(filter)]
            data['table'] = render_to_string(self.template,{'profile':profile})
        return JsonResponse(data)
