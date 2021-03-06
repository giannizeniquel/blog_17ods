"""blog_17ods URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from blog import views
from django.conf import settings
from django.conf.urls.static import static
from blog.views import SignUpView 

from blog.views import (
    SignUpView,
    PublicacionListView,
    PublicacionDetailView,
    PublicacionCreateView,
    PublicacionUpdateView,
    PublicacionDeleteView,
    CategoriaListView,
    )


urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('signup/', SignUpView.as_view(), name='signup'),
    #PUBLICACIONES
    path('', PublicacionListView.as_view(), name="list" ),
    path('categorias/', CategoriaListView.as_view(), name="categoria_list" ),
    path('create/', PublicacionCreateView.as_view(), name="create" ),
    path('<slug:pk>/detail/', PublicacionDetailView.as_view(), name="detail" ),
    path('<slug:pk>/update/', PublicacionUpdateView.as_view(), name="update" ),
    path('<slug:pk>/delete/', PublicacionDeleteView.as_view(), name="delete" ),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) #para cargar imagenes subidas por el usuario
