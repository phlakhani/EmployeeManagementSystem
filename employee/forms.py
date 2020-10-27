from django.forms import ModelForm
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Employee


class Registrationform(UserCreationForm):
    Email = forms.EmailField()    # custom field added to sign up form

    class Meta:
        model = User
        fields = ['username', 'Email', 'password1', 'password2']


class Profileform(ModelForm):
    class Meta:
        model = Employee
        fields = '__all__'


