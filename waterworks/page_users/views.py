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
from waterworks.models import Account
from .forms import AccountForm
success = 'success'
info = 'info'
error = 'error'
warning = 'warning'
question = 'question'

class Waterworks_Account(LoginRequiredMixin,TemplateView):
    template_name = 'waterworks/pages/account.html'

class Waterworks_Account_Create(LoginRequiredMixin,TemplateView):
    template_name = 'waterworks/components/account_create.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "New Account"
        return context

class Waterworks_Account_Create_AJAXView(LoginRequiredMixin,View):
    template_name = 'waterworks/forms/account_forms.html'
    def get(self, request):
        data = dict()
        form = AccountForm()
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
            form = AccountForm(request.POST,request.FILES)
            if form.is_valid():
                form.save()
                data['message_type'] = success
                data['message_title'] = 'Successfully saved.'
        return JsonResponse(data)

class Waterworks_Account_Delete_AJAXView(LoginRequiredMixin,View):
    def post(self, request,pk):
        data = dict()
        if request.method == 'POST':
            Account.objects.get(pk=pk).delete()
            data['message_type'] = success
            data['message_title'] = 'Successfully deleted.'
        return JsonResponse(data)

class Waterworks_Account_Table_AJAXView(LoginRequiredMixin,View):
    queryset = Account.objects.all()
    template_name = 'waterworks/tables/account_table.html'
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
            account = self.queryset.filter(Q(firstname__icontains = search)|Q(surname__icontains = search)).order_by('surname','firstname')[int(start):int(end)]
            data['account'] = render_to_string(self.template_name,{'account':account,'start':start})
        return JsonResponse(data)
