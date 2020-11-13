from django import forms
from .models import Car
from django.contrib.auth.models import User
from django.forms.widgets import SelectDateWidget


class CarForm(forms.ModelForm):

    MONTHS = {
        1: ('Enero'), 2: ('Febrero'),
        3: ('Marzo'), 4: ('Abril'),
        5: ('Mayo'), 6: ('Junio'),
        7: ('Julio'), 8: ('Agosto'),
        9: ('Septiembre'), 10: ('Octubre'),
        11: ('Noviembre'), 12: ('Diciembre')
    }

    date = forms.DateField(
                widget=SelectDateWidget(
                    empty_label=("Año", "Mes", "Día"),
                    months=MONTHS
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
            'schedule',
            'date'
            ]
        labels = {
            'provider': 'Mecánico',
            'brand': 'Marca',
            'car_model': 'Modelo',
            'year': 'Año',
            'transmission': 'Transmisión',
            'schedule': 'Horario',
            'date': 'Fecha'
        }
    def __init__(self, *args, **kwargs):
        super().__init__(*args,**kwargs)
        self.fields['provider'].queryset= User.objects.filter(is_staff=True)


class CarStaffForm(forms.ModelForm,):

    date = forms.DateField(
                widget=SelectDateWidget(
                    empty_label=("Año", "Mes", "Día")
                )
            )

    class Meta:
        model = Car
        fields = [
			'user',
            'provider',
            'brand',
            'car_model',
            'year',
            'transmission',
            'schedule'
            ]
        labels = {
			'user':'Cliente',
            'provider': 'Mecánico',
            'brand': 'Marca',
            'car_model': 'Modelo',
            'year': 'Año',
            'transmission': 'Transmisión',
            'schedule': 'Horario'
        }
    def __init__(self, *args, **kwargs):
        super().__init__(*args,**kwargs)
        self.fields['provider'].queryset= User.objects.filter(is_staff=True)
        self.fields['user'].queryset= User.objects.filter(is_staff= False)
