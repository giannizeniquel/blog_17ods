from django.contrib import admin
from django.contrib.auth.models import Group
from django.db import models
from django.db.models import CharField
from django.db.models.functions import Cast
from django.db.models.fields import CharField
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
    
@admin.register(User)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('id','username', 'first_name', 'last_name', 'rol', 'is_superuser', 'get_groups',)

    #obtengo los grupos que estan en una tabla intermedia
    def get_groups(self, obj):
        l = obj.groups.values_list('name', flat = True) # QuerySet Object
        l_as_list = list(l)
        return l_as_list
    
    #para darle formato al head de la tabla
    get_groups.short_description = 'Grupo'

#formato por defecto del sitio admin
#admin.site.register(Estado)
#admin.site.register(Rol)
#admin.site.register(User)
#admin.site.register(Categoria)
#TODO: seguir customizando vistas pagina admin
admin.site.register(Publicacion)
admin.site.register(Comentario)
