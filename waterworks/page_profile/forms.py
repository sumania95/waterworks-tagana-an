from django import forms
from django.forms import ModelForm
from waterworks.models import (
    Profile,
    Barangay,
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
