from django import forms
from django.forms import ModelForm
from waterworks.models import (
    Year,
)

class YearForm(forms.ModelForm):
    class Meta:
        model = Year
        fields = [
            'name',
        ]
