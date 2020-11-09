from django import forms
from .models import Car
from django.contrib.auth.models import User


class CreateNewList(forms.Form):
	name = forms.CharField(label="Name ", max_length=300)

class CarForm(forms.ModelForm):

    class Meta:
        model = Car
        fields = ['provider', 'car_model', 'transmission', 'year', 'brand']
        labels = {'provider': 'Provider', 'car_model': 'Car_model', 'transmission': 'Transmission', 'year': 'Year', 'brand': 'Brand'}
    def __init__(self, *args, **kwargs):
        super().__init__(*args,**kwargs)
        self.fields['provider'].queryset= User.objects.filter(is_staff=True)
