from django import forms
from .models import Car


class CarForm(forms.ModelForm):

    class Meta:
        model = Car
        fields = [
            'car_model',
            'transmission',
            'year',
            'brand',
            ]
        labels = {
            'car_model': 'Car_model',
            'transmission': 'Transmission',
            'year': 'Year',
            'brand': 'Brand',
        }
