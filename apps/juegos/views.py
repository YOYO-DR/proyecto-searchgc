import codecs

from django.http import HttpResponseRedirect,JsonResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import View

from .functions import obtenerCara,guardarCara


class ProcesarDatos(View):
    def dispatch(self, request, *args, **kwargs):
        if request.method=='GET':
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
        cara=obtenerCara(data)
        guardarCara(cara)
        return JsonResponse(cara)

def prueba(request):
    return render(request,'plt/hambur.html')