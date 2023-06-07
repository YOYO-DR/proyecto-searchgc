from django.views.generic import TemplateView
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import FormView
from django.contrib.auth.forms import AuthenticationForm
from django.urls import reverse_lazy
from django.contrib.auth import login,logout,authenticate
from .forms import crearUsuario
from django.shortcuts import redirect,render

class InicioView(TemplateView):
  template_name = 'inicio.html'

  def get_context_data(self, **kwargs):
      context = super().get_context_data(**kwargs)
      context["titulo"] = 'Inicio'
      context["dato"] = 'Este va a ser la pagina inicial del proyecto'
      return context


# def registrar(request):
#   context = {
#     'titulo':'Registrarse',
#     'id':0
#   }
#   if request.method == 'GET':
#     context={'form':crearUsuario,
#              'titulo':'Registrarse'}
#     return render(request,'registro.html',context)
#   else:
#     if request.POST['password1']==request.POST['password2']:
#       if re.match(r'^([a-zA-Z0-9._%-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,})$',request.POST['email']):
#         try:
#           user=User.objects.create_user(username=request.POST['username'],password=request.POST['password1'],email=request.POST['email'])
#           user.save()
#           login(request,user)
#           return redirect('inicio:inicio')
#         except IntegrityError as e:
#           return render(request,'registro.html',{
#             'form': crearUsuario,
#             'error':'El usuario ya existe',
#             'titulo':'Registrarse'
#             })
#       else:
#         return render(request,'registro.html',{
#             'form': crearUsuario,
#             'error':'El correo no es valido',
#             'titulo':'Registrarse'
#             })

class RegitroFormView(FormView):
  form_class = crearUsuario
  template_name = 'registro.html'
  success_url = reverse_lazy('inicio:inicio')

  def dispatch(self, request, *args, **kwargs):
    #antes de entrar a la pagina reviso que no este autenticado, si lo esta, lo mando al inicio
    if request.user.is_authenticated:
      return redirect('inicio:inicio')
    return super().dispatch(request, *args, **kwargs)

  def form_valid(self, form):
    form.save()
    user = form.cleaned_data['username']
    passw = form.cleaned_data['password1']
    user=authenticate(username=user, password=passw)
    #si es correcto el formulario, inicio sesión
    login(self.request, user)
    return HttpResponseRedirect(self.success_url)
  
  def form_invalid(self, form):
    for i in form.errors:
      print(i)
    return super().form_invalid(form)
  
  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    context['title'] = 'Iniciar sesión'
    return context


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