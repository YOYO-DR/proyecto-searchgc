import codecs

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView

from .functions import obtenerCara


class ProcesarDatos(TemplateView):
    template_name = 'caracteristicas.html'
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
           inicio = reverse_lazy('inicio:iniciarsesion')
           return HttpResponseRedirect(inicio)
        return super().dispatch(request, *args, **kwargs)


    def post(self, request, *args, **kwargs):
        archivo=request.FILES['archivo']
        lineas=archivo.readlines()
        data = []
        for linea in lineas:
           linea_decodificada=linea.decode('utf-8',errors='ignore')
           data.append(linea_decodificada)
        self.caracteristicas=obtenerCara(data)
        graficas=''
        rams=''
        procesadores=''
        sisOpe=''
        discos=''
        # for cara in caracteristicas:
        #   print('-'*10+str(len(cara)-1),end=' ')
        #   for parte in cara:
        #     if isinstance(parte, str):
        #       print(parte+'-'*10)
        #       continue
        #     print('-'*5)
        #     for clave,valor in parte.items():
        #       print(f'{clave}: {valor}')

    