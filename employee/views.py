from django.contrib.auth import authenticate, login
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from .models import  Employee
from django.views.generic import ListView
from .forms import Registrationform
from django.views.generic.edit import CreateView


class Displayemployees(ListView):
    model = Employee
    template_name = 'employee_list.html'

class Signup(SuccessMessageMixin,CreateView):
    form_class = Registrationform
    template_name = 'employee_signup.html'
    success_url = reverse_lazy('list')
    success_message = 'You have successfully Signed up !'









