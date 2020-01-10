from django import forms
from django.contrib.auth.forms import UserCreationForm

class LoginForm(forms.Form):
    username = forms.CharField(max_length=45, label='Username',widget=forms.TextInput(attrs={
        'class':'form-control',
        'type':'text',
        'placeholder':'Username'
    }))
    password = forms.CharField(max_length=45, label='Password', widget=forms.TextInput(attrs={
        'class':'form-control',
        'type':'password',
        'placeholder':'Password'
    }))



class RegisterForm(forms.Form):
    GENDER_CHOISE=(
        ('L','Male'),
        ('P','Female')
    )
    username = forms.CharField(max_length=45, widget=forms.TextInput(attrs={
        'class': 'form-control'
    }))

    password = forms.CharField(max_length=45, widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Password',
        'type': 'password'
    }))
    password_confirmation = forms.CharField(max_length=45, label='Password Confirmation', widget=forms.TextInput(attrs={
        'class': 'form-control',
        'type': 'password',
        'placeholder': 'Password Confirmation'
    }))
    first_name = forms.CharField(max_length=45, label='First Name', widget=forms.TextInput(attrs={
        'class': 'form-control',
        'type': 'text',
        'placeholder': 'First Name'
    }))
    last_name = forms.CharField(max_length=45, label='Last Name', widget=forms.TextInput(attrs={
        'class': 'form-control',
        'type': 'text',
        'placeholder': 'Last Name'
    }))
    no_telepon = forms.CharField(max_length=15,label= 'Phone Number',widget=forms.TextInput(attrs={
        'class':'form-control',
        'type':'text',
        'placeholder':'Phone Number'
    }))
    nik_customers = forms.CharField(max_length=45, label='NIK', widget=forms.TextInput(attrs={
        'class': 'form-control',
        'type': 'text',
        'placeholder': 'NIK'
    }))
    gender = forms.ChoiceField(widget=forms.Select(),choices=GENDER_CHOISE,initial='L',required=True)
    photo_profile = forms.ImageField()