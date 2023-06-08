from django.db import models
from django.contrib.auth.models import AbstractUser
from config.settings import MEDIA_URL,STATIC_URL
class User(AbstractUser):
    email = models.EmailField(null=False, blank=False,unique=True,verbose_name='Correo electrónico')
    imagen=models.ImageField(upload_to='users/Y%/m%/',null=True,blank=True, verbose_name='Foto de perfil')

    def get_image(self):
        if self.imagen:
            return f'{MEDIA_URL}{self.imagen}'
        return f'{STATIC_URL}media/img/empty.png'