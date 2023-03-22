from django.contrib import admin
from django.urls import path,include
from .views import *
from django.contrib.auth.views import LogoutView
from user import views
urlpatterns = [
 
    path('managerregister/',ManagerRegisterView.as_view(),name='managerregister'),
    path('developerregister/',DeveloperRegisterView.as_view(),name='developerregister'),
    path('login/',UserLoginView.as_view(),name='login'),
    path('logout/',UserLogoutView.as_view(),name='logout'),
    path('dashboard/',dashboard,name='dashboard'),
    
    # path('home/' ,home,name='home'),

]