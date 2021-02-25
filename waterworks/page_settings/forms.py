from django import forms
from django.forms import ModelForm
from waterworks.models import (
    Settings,
)

class SettingsForm(forms.ModelForm):
    class Meta:
        model = Settings
        fields = [
            'application_name',
            'address',
        ]
