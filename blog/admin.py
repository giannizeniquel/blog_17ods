from django.contrib import admin
from .models import Estado, Rol, User, Categoria, Publicacion, Comentario

# Register your models here.
admin.site.register(Estado)
admin.site.register(Rol)
admin.site.register(User)
admin.site.register(Categoria)
admin.site.register(Publicacion)
admin.site.register(Comentario)
