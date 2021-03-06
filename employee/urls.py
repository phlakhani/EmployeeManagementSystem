from django.urls import path
from django.contrib.auth import views as auth_view
from .views import  Displayemployees, Signup, Profileview, editProfile


urlpatterns = [
    path('', Displayemployees, name='home'),
    path('signup/', Signup ,name='signup',),
    path('login/', auth_view.LoginView.as_view(template_name='employee_login.html') ,name='login'),
    path('logout/', auth_view.LogoutView.as_view(template_name='employee_logout.html') ,name='logout'),
    path('create_profile/', Profileview, name='create_profile'),
    path('updateprofile/<int:pk>', editProfile, name='update_profile'),
]