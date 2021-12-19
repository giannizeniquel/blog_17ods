from typing import AbstractSet
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser

# Create your models here.

class Estado(models.Model):
    activo = models.BooleanField(default=True)
    
    def __str__(self) -> str:
        return self.activo
    
class Rol(models.Model):
    estado = models.ForeignKey(Estado, on_delete=models.PROTECT)
    nombre_rol = models.CharField(max_length=50)
    descripcion_rol = models.TextField(null=True, blank=True)
    
    def __str__(self) -> str:
        return self.nombre_rol
    
class User(AbstractUser):
    rol = models.ForeignKey(Rol, on_delete=models.PROTECT, null=True)
    estado = models.ForeignKey(Estado, on_delete=models.PROTECT, default=1)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    fecha_nac = models.DateField(null=True, blank=True)
    descripcion = models.TextField(null=True, blank=True)
    
    def __str__(self) -> str:
        return self.username
    
class Categoria(models.Model):
    nombre = models.CharField(max_length=200)
    cant_publ = models.IntegerField(default=0)
    
    def __str__(self) -> str:
        return self.nombre

class Publicacion (models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    categoria = models.ForeignKey(Categoria, on_delete=models.PROTECT)
    estado = models.ForeignKey(Estado, on_delete=models.PROTECT)
    titulo = models.CharField(max_length=200)
    sub_titulo = models.CharField(max_length=400)
    contenido = models.TextField()
    fecha_hora_publ = models.DateTimeField(auto_now_add = True)
    fecha_edicion = models.DateTimeField(auto_now = True)
    cantidad_coment = models.IntegerField(default=0)
    imagen = models.ImageField(upload_to='images')
    
    def publicar(self):
        self.fecha_hora_publ = timezone.now()
        self.save()
        
    def __str__(self) -> str:
        return self.titulo

    class Meta:
        verbose_name = ("Publicacion")
        verbose_name_plural = ("Publicaciones")
  
class Comentario(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    estado = models.ForeignKey(Estado, on_delete=models.PROTECT)
    publicacion = models.ForeignKey(Publicacion, on_delete=models.CASCADE)
    titulo = models.CharField(max_length=200)
    contenido = models.TextField()
    fecha_hora_coment = models.DateTimeField(auto_now_add = True)
    
    def __str__(self) -> str:
        return self.user.nombre_usuario
    
    class Meta:
        verbose_name = ("Comentario")
        verbose_name_plural = ("Comentarios")
    

