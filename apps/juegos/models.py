from django.db import models

from apps.user.models import User

class UrlJuegos(models.Model):
    url = models.TextField(null=False, blank=False)
    nombreJuego = models.CharField(max_length=100,null=False,blank=False)

    class Meta:
        verbose_name = 'Url Juego'
        verbose_name_plural = 'Url Juegos'

class Telefonos(models.Model):
    numeroTelefono=models.CharField(max_length=20,null=False, blank=False)
    usuario=models.ForeignKey(User,on_delete=models.CASCADE,null=False,blank=False)

    class Meta:
        verbose_name = 'Telefono'
        verbose_name_plural = 'Telefonos'

class Favoritos(models.Model):
    usuario=models.ForeignKey(User,on_delete=models.CASCADE,null=False,blank=False)

    class Meta:
        verbose_name = 'Favorito'
        verbose_name_plural = 'Favoritos'

class Favoritos_UrlJuegos(models.Model):
    favorito = models.ForeignKey(Favoritos,on_delete=models.CASCADE,null=False,blank=False)
    urlJuego = models.ForeignKey(UrlJuegos,on_delete=models.CASCADE,null=False,blank=False)

    class Meta:
        verbose_name = 'Favorito_urlJuego'
        verbose_name_plural = 'Favoritos_urlJuegos'

class Historiales(models.Model):
    busqueda = models.CharField(max_length=100,null=False,blank=False)
    fechaBusqueda=models.DateField(auto_now_add=True)
    usuario=models.ForeignKey(User,on_delete=models.CASCADE,null=False,blank=False)

    class Meta:
        verbose_name = 'Historial'
        verbose_name_plural = 'Historiales'

class RamsVelocidades(models.Model):
    velocidadMhz = models.IntegerField(null=False, blank=False)

    class Meta:
        verbose_name = 'Ram Velocidad'
        verbose_name_plural = 'Rams Velocidades'

class TipoRam(models.Model):
    nombre=models.CharField(max_length=10,null=False, blank=False)

    class Meta:
        verbose_name = 'Tipo ram'
        verbose_name_plural = 'Tipos rams'

class Rams(models.Model):
    gb=models.IntegerField(null=False, blank=False)
    tipo=models.ForeignKey(TipoRam, on_delete=models.CASCADE ,null=False, blank=False)
    velocidad = models.ForeignKey(RamsVelocidades,on_delete=models.CASCADE,null=True,blank=True)

    class Meta:
        verbose_name = 'Ram'
        verbose_name_plural = 'Rams'

class Procesadores(models.Model):
    nombre = models.CharField(max_length=100,null=False, blank=False)
    nucleos=models.IntegerField(null=False, blank=False)
    hilos=models.IntegerField(null=False, blank=False)
    ghz=models.DecimalField(max_digits=3,decimal_places=1,null=False, blank=False)

    class Meta:
        verbose_name = 'Procesador'
        verbose_name_plural = 'Procesadores'

class SistemasOperativos(models.Model):
    nombre = models.CharField(max_length=100,null=False, blank=False,unique=True)

    class Meta:
        verbose_name = 'Sistema Operativo'
        verbose_name_plural = 'Sistema Operativos'

class GraficasGb(models.Model):
    gb=models.DecimalField(max_digits=9,decimal_places=2,null=False, blank=False)

    class Meta:
        verbose_name = 'Grafica gb'
        verbose_name_plural = 'Graficas gb'

class GraficasVelocidades(models.Model):
    velocidadMhz=models.IntegerField(null=False, blank=False)

    class Meta:
        verbose_name = 'Grafica velocidad'
        verbose_name_plural = 'Graficas velocidades'

class Graficas(models.Model):
    nombre = models.CharField(max_length=100,null=False, blank=False)
    nucleos=models.IntegerField(null=True, blank=True)
    gb=models.ForeignKey(GraficasGb,on_delete=models.CASCADE,null=True, blank=True)
    velocidad=models.ForeignKey(GraficasVelocidades,on_delete=models.CASCADE,null=True,blank=True)

    class Meta:
        verbose_name = 'Grafica'
        verbose_name_plural = 'Graficas'

class Dispositivos(models.Model):
    espacioGb = models.IntegerField(null=False,blank=False)
    nombre = models.CharField(max_length=200,null=True,blank=True)
    usuario=models.ForeignKey(User,on_delete=models.CASCADE,null=False,blank=False)
    procesador=models.ForeignKey(Procesadores,on_delete=models.CASCADE,null=False,blank=False)
    ram=models.ForeignKey(Rams,on_delete=models.CASCADE,null=False,blank=False)
    grafica=models.ForeignKey(Graficas,on_delete=models.CASCADE,null=False,blank=False)
    sistemaOperativo=models.ForeignKey(SistemasOperativos,on_delete=models.CASCADE,null=False,blank=False)

    class Meta:
        verbose_name = 'Dispositivo'
        verbose_name_plural = 'Dispositivos'