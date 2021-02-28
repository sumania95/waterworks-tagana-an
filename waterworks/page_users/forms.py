from django import forms
from django.forms import ModelForm
from waterworks.models import (
    Account,
)

class AccountForm(forms.ModelForm):
    class Meta:
        model = Account
        fields = [
            'surname',
            'firstname',
            'middlename',
            'is_admin',
        ]
