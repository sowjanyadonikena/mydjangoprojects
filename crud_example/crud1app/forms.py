from django import forms
from .models import RunCodes

class RCForm(forms.ModelForm):
    class Meta():
        model = RunCodes
        fields = '__all__'