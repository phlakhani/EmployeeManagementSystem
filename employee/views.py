from django.shortcuts import render, redirect
from django.contrib import messages
from django.views.generic import ListView
from django.views.generic.edit import FormView
from django.contrib.auth.decorators import login_required

from .models import  Employee
from .forms import Registrationform, Profileform


def Displayemployees(request):

    employees = Employee.objects.all()
    HadProfileUsers = [e.username for e in employees]
    
    context = {
        'employees': employees,
        'HadProfileUsers':str(HadProfileUsers)
    }
    return render(request, 'employee_list.html',context)


def Signup(request):
    if request.method == 'POST':
        form = Registrationform(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request,f'Account created for {username}')
            return redirect('home')
    else:
        form = Registrationform()
    return render(request, 'employee_signup.html',{'form':form})


@login_required(login_url='login')
def Profileview(request):
    if request.method == 'POST':
        form = Profileform(request.POST)
        if form.is_valid():
            form.save()
            name = form.cleaned_data.get('name')
            messages.success(request, f'Profile created for {name}')
            return redirect('home')
    else:
        form = Profileform()
    return render(request,'employee_profile.html',{'form':form})



@login_required(login_url='login')
def editProfile(request, pk):
    user = Employee.objects.get(id=pk)
    form = Profileform(instance=user)

    if request.method == 'POST':
        form = Profileform(request.POST, instance=user)
        if form.is_valid():
            form.save()
        return ('home')
    else:
        context = { 'form':form }
        return render(request, 'edit_profile.html', context)













# class Profileview(FormView):
#     form_class = Profileform()
#     template_name = 'employee_profile.html'
#     success_url = '/home/'
#
#     def form_valid(self, form):
#         # This method is called when valid form data has been POSTed.
#         # It should return an HttpResponse.
#         form.save()
#         return super().form_valid(form)










