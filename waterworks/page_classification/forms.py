from django import forms
from django.forms import ModelForm
from waterworks.models import (
    Classification,
)

class ClassificationForm(forms.ModelForm):
    class Meta:
        model = Classification
        fields = [
            'name',
        ]
