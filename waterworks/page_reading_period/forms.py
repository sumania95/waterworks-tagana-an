from django import forms
from django.forms import ModelForm
from waterworks.models import (
    Reading_Period,
)

class Reading_PeriodForm(forms.ModelForm):
    class Meta:
        model = Reading_Period
        fields = [
            'month',
            'due_date',
            'disconnection_date',
        ]

class Reading_Period_UpdateForm(forms.ModelForm):
    class Meta:
        model = Reading_Period
        fields = [
            'due_date',
            'disconnection_date',
        ]
