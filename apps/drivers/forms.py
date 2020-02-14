from django import forms
from .models import Drivers
from django.contrib.auth.models import User

class DriverForm(forms.Form):
    driver_id = forms.CharField(widget=forms.HiddenInput(),required=False)
    username = forms.CharField(max_length=25,label='Username',widget=forms.TextInput(attrs={
        'class':'form-control',
        'placeholder':'username'
    }))

    password = forms.CharField(max_length=25,label='Password',widget=forms.TextInput(attrs={
        'class':'form-control',
        'placeholder':'password',
        'type':'password'
    }))

    password2 = forms.CharField(max_length=25,label='Password Confirmation',widget=forms.TextInput(attrs={
        'class':'form-control',
        'placeholder':'Password Confirmation',
        'type':'password'
    }))

    first_name = forms.CharField(max_length=45,label='First Name',widget=forms.TextInput(attrs={
        'class':'form-control',
        'placeholder':'first name'
    }))

    last_name = forms.CharField(max_length=45,label='Last Name',widget=forms.TextInput(attrs={
        'class':'form-control',
        'placeholder':'last name'
    }))

    nik_driver = forms.CharField(max_length=45,label='NIK Driver',widget=forms.TextInput(attrs={
        'class':'form-control',
        'placeholder':'nik driver'
    }))

    driver_phone_number = forms.CharField(max_length=45,label='Phone Number',widget=forms.TextInput(attrs={
        'class':'form-control',
        'placeholder':'phone number '
    }))
    
    sim_number = forms.CharField(max_length=45,label='SIM Number',widget=forms.TextInput(attrs={
        'class':'form-control',
        'placeholder':'sim number'
    }))

    sim_pict = forms.ImageField()
    ktp_pict = forms.ImageField()
    photo_profile = forms.ImageField()

