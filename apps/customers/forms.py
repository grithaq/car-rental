from django import forms


class UserForm(forms.Form):
    id = forms.CharField(widget=forms.HiddenInput(),required=False)
    username = forms.CharField(max_length=12,label='Username',widget=forms.TextInput(attrs={
        'class':'form-control',
        'placeholder':'Username'
    }))
    password = forms.CharField(max_length=13,label='Password',widget=forms.TextInput(attrs={
        'class':'form-control',
        'placeholder':'Password',
        'type':'password'
    }))
    password_confirmation = forms.CharField(max_length=13,label='Password Confirmation',widget=forms.TextInput(attrs={
        'class':'form-control',
        'placeholder':'Password',
        'type':'password'
    }))
    first_name = forms.CharField(max_length=45,label='First Name',widget=forms.TextInput(attrs={
        'class':'form-control',
        'placeholder':'First Name',
        'type':'text'
    }))
    last_name = forms.CharField(max_length=45,label='Last Name',widget=forms.TextInput(attrs={
        'class':'form-control',
        'placeholder':'Last Name',
        'type':'text'
    }))
    photo_profile = forms.ImageField(label='Photos')


class CreateCustomerForm(forms.Form):
    id = forms.CharField(widget=forms.TextInput(),required=False)
    GENDER_CHOISE=(
        ('L','Male'),
        ('P','Female')
    )
    username = forms.CharField(max_length=45, widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder' :'Username'
    }))

    password = forms.CharField(max_length=45, widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Password',
        'type': 'password'
    }),required=False)
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
    photo_profile = forms.ImageField(required=False)
class EditCustomers(forms.Form):
    pass

class EditDetail(forms.Form):
    GENDER = (
        ('L','Male'),
        ('P','Female')
    )
    id = forms.CharField(widget=forms.HiddenInput())
    first_name = forms.CharField(label='First Name',max_length=45,widget=forms.TextInput(attrs={
        'class':'form-control',
        'placeholder':'first name'
    }))
    last_name = forms.CharField(label='Last Name',max_length=45,widget=forms.TextInput(attrs={
        'class':'form-control',
        'placeholder':'last name'
    }))
    no_telepon = forms.CharField(label='Phone Number',max_length=45,widget=forms.TextInput(attrs={
        'class':'form-control',
        'placeholder':'phone number'
    }))
    nik_customers = forms.CharField(label='NIK',max_length=45,widget=forms.TextInput(attrs={
        'class':'form-control',
        'placeholder':'nik customer'
    }))
    gender = forms.ChoiceField(choices=GENDER,label='Gender',initial='L',required=True)
    photo_profile = forms.ImageField(required=False)