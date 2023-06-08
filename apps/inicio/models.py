from django.db import models
from apps.user.models import User

class UrlJuegos(models.Model):
    url = models.TextField(null=False, blank=False)
    nombreJuego = models.CharField(max_length=100,null=False,blank=False)

class Telefonos(models.Model):
    numeroTelefono=models.CharField(max_length=20,null=False, blank=False)
    usuario=models.ForeignKey(User,on_delete=models.CASCADE,null=False,blank=False)

class Favoritos(models.Model):
    usuario=models.ForeignKey(User,on_delete=models.CASCADE,null=False,blank=False)

class Favoritos_UrlJuegos(models.Model):
    favorito = models.ForeignKey(Favoritos,on_delete=models.CASCADE,null=False,blank=False)
    urlJuego = models.ForeignKey(UrlJuegos,on_delete=models.CASCADE,null=False,blank=False)

class Historiales(models.Model):
    busqueda = models.CharField(max_length=100,null=False,blank=False)
    fechaBusqueda=models.DateField(auto_now_add=True)
    usuario=models.ForeignKey(User,on_delete=models.CASCADE,null=False,blank=False)

class RamsVelocidades(models.Model):
    velocidadMhz = models.IntegerField(null=False, blank=False)

class Rams(models.Model):
    gb=models.IntegerField(null=False, blank=False)
    velocidad = models.ForeignKey(RamsVelocidades,on_delete=models.CASCADE,null=False,blank=False)

class Procesadores(models.Model):
    nombre = models.CharField(max_length=100,null=False, blank=False)
    nucleos=models.IntegerField(null=False, blank=False)
    hilos=models.IntegerField(null=False, blank=False)
    ghz=models.DecimalField(max_digits=3,decimal_places=1,null=False, blank=False)

class SistemasOperativos(models.Model):
    nombre = models.CharField(max_length=100,null=False, blank=False,unique=True)

class GraficasGb(models.Model):
    gb=models.DecimalField(max_digits=9,decimal_places=2,null=False, blank=False)

class GraficasVelocidades(models.Model):
    velocidadMhz=models.IntegerField(null=False, blank=False)

class Graficas(models.Model):
    nombre = models.CharField(max_length=100,null=False, blank=False)
    gb=models.ForeignKey(GraficasGb,on_delete=models.CASCADE,null=False,blank=False)
    velocidad=models.ForeignKey(GraficasVelocidades,on_delete=models.CASCADE,null=False,blank=False)

class Dispositivos(models.Model):
    espacioGb = models.IntegerField(null=False,blank=False)
    nombre = models.CharField(max_length=200,null=True,blank=True)
    usuario=models.ForeignKey(User,on_delete=models.CASCADE,null=False,blank=False)
    procesador=models.ForeignKey(Procesadores,on_delete=models.CASCADE,null=False,blank=False)
    ram=models.ForeignKey(Rams,on_delete=models.CASCADE,null=False,blank=False)
    grafica=models.ForeignKey(Graficas,on_delete=models.CASCADE,null=False,blank=False)
    sistemaOperativo=models.ForeignKey(SistemasOperativos,on_delete=models.CASCADE,null=False,blank=False)