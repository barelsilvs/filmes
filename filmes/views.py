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


# def home(request):
#     noticias = Noticia.objects.all()
#     return render(request, 'home.html', {"noticias": noticias})

class FilmeListView(ListView):
    model=Filme
    template_name='filme/listar.html'
    context_object_name='filmes'
    ordering='-nome'


# def listar(request):
#     autores = Autor.objects.all().order_by('-nome')
#     return render(request, 'listar.html', {'autores':autores})

class FilmeDetailView(DetailView):
    model=Filme
    template_name='filme/detalhar.html'
    context_object_name='filme'
    pk_url_kwarg='id'


# def detalhar(request, id):
#     autor = Autor.objects.get(id=id)
#     return render(request, 'detalhar.html', {'autor':autor})


class FilmeCreateView(CreateView):
    model=Filme
    template_name='filme/cadastrar.html'
    form_class=FilmeForm
    

    def get_success_url(self):
        messages.add_message(self.request, messages.SUCCESS, "Filme  cadastrado com sucesso!")
        return reverse('listar-filme')



# def cadastrar(request):
#     if request.method == "POST":
#         form = AutorForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             messages.add_message(request, messages.SUCCESS, "Autor cadastrado com sucesso!")
#             return redirect("listar")
#     else:
#          form = AutorForm()
#          return render(request, 'cadastrar.html', {'form': form})


class FilmeUpdateView(UpdateView):
    model=Filme
    template_name='filme/atualizar.html'
    form_class=FilmeForm
    pk_url_kwarg='id'

    def get_success_url(self):
        messages.add_message(self.request, messages.SUCCESS, "Filme atualizado com sucesso!")
        return reverse('listar-fime')


# def atualizar(request, id):
#     autor = Autor.objects.get(id=id)
#     form = AutorForm(instance=autor)
#     if request.method == "POST":
#         form = AutorForm(request.POST, request.FILES, instance=autor)
#         if form.is_valid():
#             form.save()
#             return redirect("atualizar", id=id)
#         else:
#             return render(request, 'atualizar.html', {'form': form})
#     else:
#          return render(request, 'atualizar.html', {'form': form})

class FilmeDeleteView(DeleteView):
    model=Filme
    template_name='filme/filme_confirm_delete.html'
    pk_url_kwarg='id'

    def get_success_url(self):
        messages.add_message(self.request, messages.SUCCESS, "Filme deletado com sucesso!")
        return reverse('listar-filme')


# def deletar(request, id):
#     autor = Autor.objects.get(id=id)
#     autor.delete()
#     return redirect('listar')


class MovieListView(ListView):
    model=Movie
    template_name='movie/listar.html'
    context_object_name='movies'
    ordering='-titulo'


class MovieDetailView(DetailView):
    model=Movie
    template_name='movie/detalhar.html'
    context_object_name='movie'


class MovieCreateView(CreateView):
    model=Movie
    template_name='movie/cadastrar.html'
    form_class=MovieForm
    

    def get_success_url(self):
        messages.add_message(self.request, messages.SUCCESS, "Noticia cadastrada com sucesso!")
        return reverse('listar-noticia')
    

class MovieUpdateView(UpdateView):
    model=Movie
    template_name='movie/atualizar.html'
    form_class=MovieForm

    def get_success_url(self):
        messages.add_message(self.request, messages.SUCCESS, "movie atualizada com sucesso!")
        return reverse('listar-movie')
    

class MovieDeleteView(DeleteView):
    model=Movie
    template_name='movie/movie_confirm_delete.html'

    def get_success_url(self):
        messages.add_message(self.request, messages.SUCCESS, "Movie deletada com sucesso!")
        return reverse('listar-movie')