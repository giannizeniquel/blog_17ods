from django.shortcuts import redirect, render
from .models import *
from .forms import UserRegisterForm, PublicacionForm, ComentarioForm
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
    
    def post(self, *args, **kwargs):
        form = ComentarioForm(self.request.POST)
        if form.is_valid():
            post = self.get_object()
            comentario = form.instance
            comentario.usuario = self.request.user
            comentario.publicacion = post
            comentario.save()
            return redirect('detail', post.id)
        else:
            return redirect('detail', self.get_object().id)
            
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'form': ComentarioForm
        })
        return context
class PublicacionCreateView(CreateView):
    form_class = PublicacionForm
    model = Publicacion
    
    def form_valid(self, form):
        post = form.instance
        post.usuario = self.request.user 
        post.save()
        return redirect('detail', post.id)
        
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'nombre_vista': 'Publicar'
        })
        return context


class PublicacionUpdateView(UpdateView):
    form_class = PublicacionForm
    model = Publicacion
    success_url = reverse_lazy('list')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'nombre_vista': 'Editar'
        })
        return context

    
class PublicacionDeleteView(DeleteView):
    model = Publicacion
    success_url = reverse_lazy('list')
    
class CategoriaListView(ListView):
    model = Categoria
