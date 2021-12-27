from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import *
#para usar mi User custom
from django.contrib.auth import get_user_model
User = get_user_model() 

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repite contraseña', widget=forms.PasswordInput)
    
    class Meta:
        model= User
        fields = [ 'username', 'email', 'password1', 'password2', 'first_name', 'last_name', 'biografia', 'imagen' ]
        help_texts = { k:"" for k in fields }
        
class PublicacionForm(forms.ModelForm):
    class Meta:
        model = Publicacion
        fields = (
            'categoria',
            'titulo',
            'sub_titulo',
            'contenido',
            'imagen',
            'es_publico',
        )

class ComentarioForm(forms.ModelForm):
    contenido = forms.CharField(required = True, widget=forms.Textarea(attrs={
        'rows': 4
    }))
    class Meta:
        model = Comentario
        fields = (
            'titulo',
            'contenido',
        )
        