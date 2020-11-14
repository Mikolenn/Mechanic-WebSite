from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User

# class RegisterForm(UserCreationForm):
#     email=forms.EmailField()
#
#     class Meta:
#         model=User
#         fields=["username", "email", "password1", "password2"]

class RegisterForm(UserCreationForm):

    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = (
            'username' ,
            'first_name' ,
            'last_name' ,
            'email' ,
            'password1' ,
            'password2'
        )

    def save(self, commit=True):
        user = super (RegisterForm , self ).save(commit=False)
        user.first_name = self.cleaned_data ['first_name']
        user.last_name = self.cleaned_data ['last_name']
        user.email = self.cleaned_data ['email']

        if commit :
            user.save()

        return user


class RegisterStaffForm(UserCreationForm):

    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = (
            'username' ,
            'first_name' ,
            'last_name' ,
            'email' ,
            'password1' ,
            'password2'
        )

    def save(self, commit=True):
        user = super (RegisterStaffForm , self ).save(commit=False)
        user.is_staff = True
        user.first_name = self.cleaned_data ['first_name']
        user.last_name = self.cleaned_data ['last_name']
        user.email = self.cleaned_data ['email']

        if commit :
            user.save()

        return user
