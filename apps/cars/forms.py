from django import  forms

class CarsForm(forms.Form):
    car_name = forms.CharField(max_length=45)
    car_type = forms.CharField(max_length=45)
    baggage = forms.CharField(max_length=45)
    passengers = forms.CharField(max_length=45)
    car_pict = forms.ImageField()