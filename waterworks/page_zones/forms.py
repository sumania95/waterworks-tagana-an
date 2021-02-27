from django import forms
from django.forms import ModelForm
from waterworks.models import (
    Reading,
)

class ReadingForm(forms.ModelForm):
    present_reading = forms.IntegerField(label='',widget=forms.NumberInput(attrs={'class':"form-control-sm"}))
    class Meta:
        model = Reading
        fields = [
            'present_reading',
        ]
