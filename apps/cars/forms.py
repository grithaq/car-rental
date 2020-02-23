from django import  forms

class CarsForm(forms.Form):
    id = forms.CharField(widget=forms.HiddenInput(),required=False)
    car_name = forms.CharField(max_length=45, label='Car Name',widget=forms.TextInput(attrs={
        'class':'form-control',
        'placeholder':'car name'
    }))
    car_brand = forms.CharField(max_length=45,label='Car Brand',widget=forms.TextInput(attrs={
        'class':'form-control',
        'placeholder':'brand'
    }))
    cargo_volume = forms.CharField(max_length=45,label='Cargo Volume',widget=forms.TextInput(attrs={
        'class':'form-control',
        'placeholder':'cargo volume'
    }))
    seating_capacity = forms.CharField(max_length=45,label='Seating Capacity',widget=forms.TextInput(attrs={
        'class':'form-control',
        'placeholder':'seating capacity'
    }))
    car_pict = forms.ImageField()
    price = forms.DecimalField(label='Price',widget=forms.NumberInput(attrs={
        'class':'form-control',
        'placeholder':'price'
    }))
class CarsEditForm(forms.Form):
    id = forms.CharField(widget=forms.HiddenInput(),required=False)
    car_name = forms.CharField(max_length=45, label='Car Name',widget=forms.TextInput(attrs={
        'class':'form-control',
        'placeholder':'car name'
    }))
    car_brand = forms.CharField(max_length=45,label='Car Brand',widget=forms.TextInput(attrs={
        'class':'form-control',
        'placeholder':'brand'
    }))
    cargo_volume = forms.CharField(max_length=45,label='Cargo Volume',widget=forms.TextInput(attrs={
        'class':'form-control',
        'placeholder':'cargo volume'
    }))
    seating_capacity = forms.CharField(max_length=45,label='Seating Capacity',widget=forms.TextInput(attrs={
        'class':'form-control',
        'placeholder':'seating capacity'
    }))
    car_pict = forms.ImageField(required=False)
    price = forms.DecimalField(label='Price',widget=forms.NumberInput(attrs={
        'class':'form-control',
        'placeholder':'price'
    }))