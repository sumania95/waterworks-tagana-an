from django import forms
from django.forms import ModelForm
from waterworks.models import (
    Meter_Installation,
)

class Meter_Installation_Cluster_Form(forms.ModelForm):
    class Meta:
        model = Meter_Installation
        fields = [
            'cluster',
        ]

class Meter_Installation_Sequence_Form(forms.ModelForm):
    class Meta:
        model = Meter_Installation
        fields = [
            'sequence',
        ]
