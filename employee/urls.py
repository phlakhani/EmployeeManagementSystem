from django.urls import path
from .views import  Displayemployees, Signup

urlpatterns = [
    path('list/', Displayemployees.as_view(), name='list'),
    path('signup/',Signup.as_view() ,name='signup')

]