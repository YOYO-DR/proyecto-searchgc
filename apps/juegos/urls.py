from django.urls import path
from .views import ProcesarDatos

app_name='juegos'

urlpatterns = [
    path('',ProcesarDatos.as_view(), name='procesar')
]
