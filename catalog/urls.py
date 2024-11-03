from django.urls import path
from . import views

urlputterns = [
    path('', views.home, name='home'),
    path('contacts/', views.contacts, name='contacts')
]
