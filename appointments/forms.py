from django import forms
from .models import Car

class CreateNewList(forms.Form):
	name = forms.CharField(label="Name ", max_length=300)

class CarForm(forms.ModelForm):

    class Meta:
        model = Car
        fields = [
            'brand',
            'car_model',
            'year',
            'transmission',
            'schedule'
            ]
        labels = {
            'brand': 'Marca',
            'car_model': 'Modelo',
            'year': 'Año',
            'transmission': 'Transmisión',
            'schedule': 'Horario'
        }
