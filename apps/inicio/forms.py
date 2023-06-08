from typing import Any, Dict
from django import forms
from django.contrib.auth.forms import UserCreationForm
from apps.inicio.models import User
import re
#creo la subclase del formulario de crear usuario para agregarle el email
class crearUsuario(UserCreationForm):
    #le paso el usuario user y los fields agregando el email
    class Meta:
        model = User
        fields = ['first_name','last_name','username', 'email', 'password1', 'password2']
        widgets = {
            'email': forms.TextInput(attrs={'id':'correo'}),
            'first_name': forms.TextInput(attrs={'required':True,'autofocus':True}),
            'last_name': forms.TextInput(attrs={'required':True})
        } 
    # def clean(self):
    #     cleaned = super().clean()
    #     data=self.data
    #     try:
    #       email = User.objects.get(email=data['email'])
    #     except:
    #         raise forms.ValidationError('El correo ya esta registrado')
    #     return cleaned