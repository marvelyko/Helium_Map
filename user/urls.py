from .views import login, register, dashboard,logout
from django.urls import path

urlpatterns = [
    path('login',login),
    path('register',register),
    path('dashboard',dashboard),
    path('logout',logout)
]