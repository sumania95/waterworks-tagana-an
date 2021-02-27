from django import forms
from django.forms import ModelForm
from waterworks.models import (
    Classification_Rates,
)

class Classification_RatesForm(forms.ModelForm):
    class Meta:
        model = Classification_Rates
        fields = [
            'consumption',
            'blocking_rate',
            'value_expression',
            'minimum',
        ]
