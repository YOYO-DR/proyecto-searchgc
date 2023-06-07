from django.shortcuts import render,redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login,logout,authenticate
from django.db import IntegrityError
from .forms import *
import re

def inicio(request):
  context = {'titulo':'Inicio',
             'dato':'Este va a ser la pagina inicial del proyecto'}
  return render(request,'inicio.html', context)

def registrar(request):
  context = {
    'titulo':'Registrarse',
    'id':0
  }
  if request.method == 'GET':
    context={'form':crearUsuario,
             'titulo':'Registrarse'}
    return render(request,'registro.html',context)
  else:
    if request.POST['password1']==request.POST['password2']:
      if re.match(r'^([a-zA-Z0-9._%-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,})$',request.POST['email']):
        try:
          user=User.objects.create_user(username=request.POST['username'],password=request.POST['password1'],email=request.POST['email'])
          user.save()
          login(request,user)
          return redirect('inicio:inicio')
        except IntegrityError as e:
          return render(request,'registro.html',{
            'form': crearUsuario,
            'error':'El usuario ya existe',
            'titulo':'Registrarse'
            })
      else:
        return render(request,'registro.html',{
            'form': crearUsuario,
            'error':'El correo no es valido',
            'titulo':'Registrarse'
            })

def iniciarSesion(request):
  if request.method == 'GET':
    context={
      'titulo':'Iniciar sesión',
      #formulario de inicio de sesión
      'form':AuthenticationForm
    }
    return render(request,'iniciarS.html',context)
  else:
    user = authenticate(request,username=request.POST['username'],password=request.POST['password'])
    if user == None:
      return render(request,'iniciarS.html',{
    'form': AuthenticationForm,
    'error':'Usuario o contraseña incorrectos',
    'titulo':'Iniciar sesión'
  })
    else:
      login(request,user)
      return redirect('inicio:inicio')
    
def cerrar(request):
  logout(request)
  return redirect('inicio:inicio')