from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User


# Formulario de registro para usuarios estándar

class RegisterForm(UserCreationForm):

    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = (
            'username',
            'first_name',
            'last_name',
            'email',
            'password1',
            'password2'
        )

    # Se guardan los datos del formulario
    def save(self, commit=True):

        user = super(RegisterForm, self).save(commit=False)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.email = self.cleaned_data['email']

        if commit:

            user.save()

        return user


# Formulario de registro para usuarios administrativos

class RegisterStaffForm(UserCreationForm):

    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = (
            'username',
            'first_name',
            'last_name',
            'email',
            'password1',
            'password2'
        )

    # Se guardan los datos del formulario
    def save(self, commit=True):

        user = super(RegisterStaffForm, self).save(commit=False)
        user.is_staff = True
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.email = self.cleaned_data['email']

        if commit:

            user.save()

        return user
