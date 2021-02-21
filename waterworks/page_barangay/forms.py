from django import forms
from django.forms import ModelForm
from waterworks.models import (
    Barangay,
)

class BarangayForm(forms.ModelForm):
    class Meta:
        model = Barangay
        fields = [
            'name',
            'is_active',
        ]
