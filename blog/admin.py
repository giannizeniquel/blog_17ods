from django.contrib import admin
from django.db import models
from .models import Estado, Rol, User, Categoria, Publicacion, Comentario

# Register your models here.

#customizamos las vistas de el sitio admin
@admin.register(Estado)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('id', 'activo',)

@admin.register(Rol)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('id', 'estado', 'nombre_rol', 'descripcion_rol',)
    
@admin.register(Categoria)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'descripcion_corta', 'descripcion', 'cant_publ',)

#admin.site.register(Estado)
#admin.site.register(Rol)
admin.site.register(User)
#admin.site.register(Categoria)
admin.site.register(Publicacion)
admin.site.register(Comentario)
