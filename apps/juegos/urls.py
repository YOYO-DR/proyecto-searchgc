from django.urls import path
from .views import ProcesarDatos,prueba

app_name='juegos'

urlpatterns = [
    path('',ProcesarDatos.as_view(), name='procesar'),
    path('pruebas/',prueba,name='prueba')
]
