from django.shortcuts import render,redirect,get_object_or_404
from django.views.generic import (
    View,
    TemplateView,
    ListView,
    DetailView,
)
from django.urls import reverse
#auth
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.models import User
from django.contrib.auth import logout
from django.contrib.auth.views import LoginView

#JSON AJAX
from django.template.loader import render_to_string
from django.http import JsonResponse
from django.template import RequestContext
from django.contrib.auth.mixins import LoginRequiredMixin
# Models
from waterworks.models import Account
from .forms import CustomAuthenticationForm
success = 'success'
info = 'info'
error = 'error'
warning = 'warning'
question = 'question'

class Waterworks_Login(LoginView):
    template_name = 'waterworks/auth/login.html'
    form_class = CustomAuthenticationForm

    def get_success_url(self,*args,**kwargs):
        return reverse('waterworks_home')

class Waterworks_Logout(LoginRequiredMixin,View):
    redirect_field_name = 'redirect_to'
    def get(self, request):
        logout(request)
        return redirect('waterworks_login')
