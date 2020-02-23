from django import forms
from .models import *

class AdminRentalForm(forms.Form):
    id = forms.CharField(widget=forms.HiddenInput(),required=False)
    customer = forms.ModelChoiceField(Customers.objects.all(),label='Customer',widget=forms.Select(attrs={
        'class':'form-control'
    }))
    car = forms.ModelChoiceField(Cars.objects.all(),label='Cars',widget=forms.Select(attrs={
        'class':'form-control'
    }))
    rental_date = forms.DateTimeField(label='Start Date',widget=forms.TextInput(attrs={
        'class':'form-control',
        'placeholder':'yyyy-mm-dd  HH:MM:SS'
    }))
    expire_rental_date = forms.DateTimeField(label='Expire Date',widget=forms.TextInput(attrs={
        'class':'form-control',
        'placeholder':'yyyy-mm-dd  HH:MM:SS'
    }))
    payment_pict = forms.ImageField(required=False)
    driver = forms.BooleanField(required=False)
    petrol = forms.BooleanField(required=False)
    verification = forms.BooleanField(required=False)

class RentalEditForm(forms.Form):
    id = forms.CharField(widget=forms.HiddenInput(),required=False)
    customer = forms.ModelChoiceField(Customers.objects.all(),label='Customer',widget=forms.Select(attrs={
        'class':'form-control'
    }))
    car = forms.ModelChoiceField(Cars.objects.all(),label='Cars',widget=forms.Select(attrs={
        'class':'form-control'
    }))
    rental_date = forms.DateTimeField(label='Start Date',widget=forms.TextInput(attrs={
        'class':'form-control',
        'placeholder':'yyyy-mm-dd  HH:MM:SS'
    }),required=False)
    expire_rental_date = forms.DateTimeField(label='Expire Date',widget=forms.TextInput(attrs={
        'class':'form-control',
        'placeholder':'yyyy-mm-dd  HH:MM:SS'
    }),required=False)
    payment_pict = forms.ImageField(required=False)
    driver = forms.BooleanField(required=False)
    petrol = forms.BooleanField(required=False)
    verification = forms.BooleanField(required=False)