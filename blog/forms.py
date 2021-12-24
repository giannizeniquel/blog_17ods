from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
#para usar mi User custom
from django.contrib.auth import get_user_model
User = get_user_model() 

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repite contraseña', widget=forms.PasswordInput)
    
    class Meta:
        model= User
        fields = [ 'first_name', 'last_name', 'biografia', 'imagen', 'username', 'email', 'password1', 'password1' ]
        help_texts = { k:"" for k in fields }