"""myproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from . import views

urlpatterns = [
    path('index/', views.indexpage, name='home'),
    path('login/', views.login, name='login'),

    path('login-employee/',views.login_employee,name='login-employee'),

    path('forgot-password/',views.forgot_password,name='forgot-password'),
    path('send-otp/',views.send_otp,name='send-otp'),
    path('otp/',views.otp,name='otp'),
    path('change-password/',views.chnage_password,name='change-password'),
    path('profile/',views.profile,name='profile'),
    path('e-profile/',views.e_profile,name='e-profile'),
    path('edit-profile/',views.edit_profile,name='edit-profile'),
    path('ticket/',views.ticket,name='ticket'),
    path('ticket-open/',views.ticket_open,name='ticket-open'),
    path('ticket-edit/',views.ticket_edit,name='ticket-edit'),
    path('e-logout/', views.e_logout, name='e-logout'),

    
]
