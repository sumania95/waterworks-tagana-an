from django import forms
from django.forms import ModelForm
from waterworks.models import (
    Settings,
    Modem,
)

class SettingsForm(forms.ModelForm):
    class Meta:
        model = Settings
        fields = [
            'name',
            'address',
            'logo',
            'notices',
            'water_meter_charge',
            'disconnection_charge',
            'permanently_disconnected_charge',
        ]

class ModemForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = Modem
        fields = [
            'ip_address',
            'username',
            'password',
        ]
