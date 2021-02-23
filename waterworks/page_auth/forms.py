from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from waterworks.models import Account

class CustomAuthenticationForm(AuthenticationForm):
    def confirm_login_allowed(self, user):
        if not Account.objects.filter(user__username = user.username):
            raise forms.ValidationError('Please enter a correct username and password. Note that both fields may be case-sensitive.', code='invalid_login')
        if Account.objects.filter(user__username = user.username, user__is_active = False):
            raise forms.ValidationError('Your Account has been deactivate. Contact Your Administrator', code='invalid_login')
