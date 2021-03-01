from django import forms
from django.forms import ModelForm
from waterworks.models import (
    Profile,
    Barangay,
    Meter_Installation,
    Meter_Replace,
    Meter_Status_History,
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
    def __init__(self, *args, **kwargs):
        super(ProfileForm, self).__init__(*args, **kwargs)
        self.fields['barangay']=forms.ModelChoiceField(queryset = Barangay.objects.filter(is_active=True))

class Meter_InstallationForm(forms.ModelForm):
    class Meta:
        model = Meter_Installation
        fields = [
            'meter_no',
            'reading',
        ]

class Meter_ReplaceForm(forms.ModelForm):
    class Meta:
        model = Meter_Replace
        fields = [
            'meter_no',
            'reading',
            'reason',
        ]

class Meter_DisconnectedForm(forms.ModelForm):
    class Meta:
        model = Meter_Status_History
        fields = [
            'reason',
        ]
