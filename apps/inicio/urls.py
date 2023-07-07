from django.urls import path
from apps.inicio.views import *
from django.contrib.auth.views import LogoutView

app_name='inicio'

urlpatterns = [
    path('', InicioView.as_view(),name='inicio'),
]
