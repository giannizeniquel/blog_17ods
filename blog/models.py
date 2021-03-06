from typing import AbstractSet
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser

# Create your models here.

class Estado(models.Model):
    activo = models.BooleanField(default=True)
    
    def __str__(self) -> str:
        estado = str(self.activo)
        return estado
    
class Rol(models.Model):
    estado = models.ForeignKey(Estado, on_delete=models.PROTECT, default=1)
    nombre_rol = models.CharField(max_length=50)
    descripcion_rol = models.TextField(null=True, blank=True)
    
    def __str__(self) -> str:
        return self.nombre_rol
    
class User(AbstractUser):
    rol = models.ForeignKey(Rol, on_delete=models.PROTECT, null=True, default = 1)
    estado = models.ForeignKey(Estado, on_delete=models.PROTECT, default=1)
    fecha_nac = models.DateField(null=True, blank=True)
    biografia = models.TextField(null=True, blank=True)
    imagen = models.ImageField(upload_to='images', default='images/default_user_profile.png', null=True, blank=True )
    
    class Meta:
        db_table = 'auth_user'
    
    def __str__(self) -> str:
        return self.username
    
class Categoria(models.Model):
    nombre = models.CharField(max_length=200)
    descripcion_corta = models.TextField(max_length=300, null=True, blank=True)
    descripcion = models.TextField(null=True, blank=True)
    cant_publ = models.IntegerField(default=0)
    
    def __str__(self) -> str:
        return self.nombre

class Publicacion (models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    categoria = models.ForeignKey(Categoria, on_delete=models.PROTECT)
    estado = models.ForeignKey(Estado, on_delete=models.PROTECT, default=1)
    titulo = models.CharField(max_length=200)
    sub_titulo = models.CharField(max_length=400)
    contenido = models.TextField()
    fecha_hora_publ = models.DateTimeField(auto_now_add = True)
    fecha_edicion = models.DateTimeField(auto_now = True)
    cantidad_coment = models.IntegerField(default=0)
    imagen = models.ImageField(upload_to='images')
    es_publico = models.BooleanField(default=True)
    slug = models.SlugField()
    
    def publicar(self):
        self.fecha_hora_publ = timezone.now()
        self.save()
        
    def __str__(self) -> str:
        return self.titulo

    @property
    def get_comment_count(self):
        return self.comentario_set.all().count()
    
    @property
    def comentarios(self):
        return self.comentario_set.all()

    class Meta:
        verbose_name = ("Publicacion")
        verbose_name_plural = ("Publicaciones")
  
class Comentario(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    estado = models.ForeignKey(Estado, on_delete=models.PROTECT, default=1)
    publicacion = models.ForeignKey(Publicacion, on_delete=models.CASCADE)
    titulo = models.CharField(max_length=200)
    contenido = models.TextField()
    fecha_hora_coment = models.DateTimeField(auto_now_add = True)
    
    def __str__(self) -> str:
        return self.usuario.username
    
    
    class Meta:
        verbose_name = ("Comentario")
        verbose_name_plural = ("Comentarios")
    

