from django.shortcuts import render, redirect
from django.urls import reverse
from .models import Filme, Movie
from .forms import FilmeForm, MovieForm
from django.contrib import messages
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView


# Create your views here.

class HomeTemplateView(TemplateView):
    template_name='home.html'

    def get_context_data(self, **kwargs):
        
        context = super().get_context_data(**kwargs)
        context["movies"] = Movie.objects.all()[:5]
        context["filmes"] = Filme.objects.all()[:5]
        
        return context




class FilmeListView(ListView):
    model=Filme
    template_name='filme/listar.html'
    context_object_name='filmes'
  




class FilmeDetailView(DetailView):
    model=Filme
    template_name='filme/detalhar.html'
    context_object_name='filme'
    pk_url_kwarg='id'




class FilmeCreateView(CreateView):
    model=Filme
    template_name='filme/cadastrar.html'
    form_class=FilmeForm
    

    def get_success_url(self):
        messages.add_message(self.request, messages.SUCCESS, "Filme cadastrado com sucesso!")
        return reverse('listar-filme')






class FilmeUpdateView(UpdateView):
    model=Filme
    template_name='filme/atualizar.html'
    form_class=FilmeForm
    pk_url_kwarg='id'

    def get_success_url(self):
        messages.add_message(self.request, messages.SUCCESS, "Filme atualizado com sucesso!")
        return reverse('listar-filme')




class FilmeDeleteView(DeleteView):
    model=Filme
    template_name='filme/filme_confirm_delete.html'
    pk_url_kwarg='id'

    def get_success_url(self):
        messages.add_message(self.request, messages.SUCCESS, "Filme deletado com sucesso!")
        return reverse('listar-filme')





class MovieListView(ListView):
    model=Movie
    template_name='movie/listar.html'
    context_object_name='movies'
   


class MovieDetailView(DetailView):
    model=Movie
    template_name='movie/detalhar.html'
    context_object_name='movies'


class MovieCreateView(CreateView):
    model=Movie
    template_name='movie/cadastrar.html'
    form_class=MovieForm
    

    def get_success_url(self):
        messages.add_message(self.request, messages.SUCCESS, "Movie cadastrada com sucesso!")
        return reverse('listar-movie')
    

class MovieUpdateView(UpdateView):
    model=Movie
    template_name='movie/atualizar.html'
    form_class=MovieForm

    def get_success_url(self):
        messages.add_message(self.request, messages.SUCCESS, "Movie atualizada com sucesso!")
        return reverse('listar-movie')
    

class MovieDeleteView(DeleteView):
    model=Movie
    template_name='movie/movie_confirm_delete.html'

    def get_success_url(self):
        messages.add_message(self.request, messages.SUCCESS, "Movie deletada com sucesso!")
        return reverse('listar-movie')