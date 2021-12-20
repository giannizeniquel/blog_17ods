from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from .models import Publicacion, Comentario, Categoria, Rol, Estado, User

# Create your views here.
def index(request):
    return render(request, 'index.html')

class PublicacionListView(ListView):
    model = Publicacion

class PublicacionDetailView(DetailView):
    model = Publicacion
    
class PublicacionCreateView(CreateView):
    model = Publicacion

class PublicacionUpdateView(UpdateView):
    model = Publicacion
    
class PublicacionDeleteView(DeleteView):
    model = Publicacion
