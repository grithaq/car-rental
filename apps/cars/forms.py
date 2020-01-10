from django import  forms

class CarsForm(forms.Form):
    id = forms.CharField(widget=forms.HiddenInput(),required=False)
    car_name = forms.CharField(max_length=45, label='Car Name',widget=forms.TextInput(attrs={
        'class':'form-control-sm',
    }))
    car_brand = forms.CharField(max_length=45,label='Car Brand',widget=forms.TextInput(attrs={
        'class':'form-control-sm'
    }))
    cargo_volume = forms.CharField(max_length=45,label='Cargo Volume',widget=forms.TextInput(attrs={
        'class':'form-control-sm'
    }))
    seating_capacity = forms.CharField(max_length=45,label='Seating Capacity',widget=forms.TextInput(attrs={
        'class':'form-cotrol-sm'
    }))
    car_pict = forms.ImageField()