from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class Registrationform(UserCreationForm):
    Email = forms.EmailField()    # custom field added to sign up form

    class Meta:
        model = User
        fields = ['username', 'Email', 'password1', 'password2']