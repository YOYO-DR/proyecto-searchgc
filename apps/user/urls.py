from django.urls import path
from apps.user.views import *
from django.contrib.auth.views import LogoutView

app_name='account'

urlpatterns = [
    path('registro/',RegitroView.as_view(),name='registro'),
    path('iniciarsesion/',IniciarSesionView.as_view(),name='iniciarsesion'),
    path('cerrar/',LogoutView.as_view(),name='cerrar')
]
