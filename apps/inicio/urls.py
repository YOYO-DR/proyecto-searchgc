from django.urls import path
from apps.inicio.views import *

app_name='inicio'

urlpatterns = [
    path('', InicioView.as_view(),name='inicio'),
    path('registro/',RegitroFormView.as_view(),name='registro'),
    path('iniciarsesion/',iniciarSesion,name='iniciarsesion'),
    path('cerrar/',cerrar,name='cerrar')
]
