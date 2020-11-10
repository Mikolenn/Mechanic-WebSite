from django import forms
from .models import Car
from django.contrib.auth.models import User

class CreateNewList(forms.Form):
	name = forms.CharField(label="Name ", max_length=300)

class CarForm(forms.ModelForm):

    class Meta:
        model = Car
        fields = [
            'provider',
            'brand',
            'car_model',
            'year',
            'transmission',
            'day',
            'schedule'
            ]
        labels = {
            'provider': 'Mecánico',
            'brand': 'Marca',
            'car_model': 'Modelo',
            'year': 'Año',
            'transmission': 'Transmisión',
            'day': 'Día',
            'schedule': 'Horario'
        }
    def __init__(self, *args, **kwargs):
        super().__init__(*args,**kwargs)
        self.fields['provider'].queryset= User.objects.filter(is_staff=True)