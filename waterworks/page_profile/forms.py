from django import forms
from django.forms import ModelForm
from waterworks.models import (
    Profile,
)

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = [
            'surname',
            'firstname',
            'middlename',
            'barangay',
            'classification',
        ]
