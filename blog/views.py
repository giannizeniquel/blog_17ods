from django.shortcuts import redirect, render
from .models import *
from.forms import UserRegisterForm
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

# Create your views here.
def index(request):
    return render(request, 'index.html')

class SignUpView(CreateView):
    form_class = UserRegisterForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'
    
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
