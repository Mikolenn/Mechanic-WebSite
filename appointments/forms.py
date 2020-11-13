from django import forms
from .models import Car
from django.contrib.auth.models import User
from django.forms.widgets import SelectDateWidget



class CarForm(forms.ModelForm):

    date = forms.DateField(
                widget=SelectDateWidget(
                    empty_label=("Año", "Mes", "Día")
                )
            )

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


class CarStaffForm(forms.ModelForm,):

    class Meta:
        model = Car
        fields = [
			'user',
            'provider',
            'brand',
            'car_model',
            'year',
            'transmission',
            'day',
            'schedule'
            ]
        labels = {
			'user':'Cliente',
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
        self.fields['user'].queryset= User.objects.filter(is_staff= False)
