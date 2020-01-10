from django import forms
from .models import Drivers

class DriverForms(forms.ModelForm):
    class Meta:
        model = Drivers
        fields = '__all__'