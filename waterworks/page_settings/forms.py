from django import forms
from django.forms import ModelForm
from waterworks.models import (
    Settings,
)

class SettingsForm(forms.ModelForm):
    class Meta:
        model = Settings
        fields = [
            'name',
            'address',
            'water_meter_charge',
            'disconnection_charge',
            'permanently_disconnected_charge',
        ]
