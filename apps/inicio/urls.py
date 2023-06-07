from django.urls import path
from apps.inicio.views import *

app_name='inicio'

urlpatterns = [
    path('', inicio,name='inicio'),
    path('registro/',registrar,name='registro'),
    path('iniciarsesion/',iniciarSesion,name='iniciarsesion'),
    path('cerrar/',cerrar,name='cerrar')
]
