from django.shortcuts import render, redirect, get_object_or_404
from .models import Filme
from .forms import FilmeForm
from django.contrib import messages

def home(request):
    # Lógica da sua visualização
    return render(request, 'home.html')

def listar(request):
    filmes = Filme.objects.all()
    return render(request, 'listar.html', {'filmes': filmes})


def cadastrar(request):
    if request.method == "POST":
        form = FilmeForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, "Filme cadastrado com sucesso!")
            return redirect("listar")
    else:
         form = FilmeForm()
         return render(request, 'cadastrar.html', {'form': form})
    


def atualizar(request, id):
    # Obtenha o objeto Filme com base no ID passado na URL ou retorne um erro 404 se não existir
    filme = get_object_or_404(Filme, id=id)

    if request.method == "POST":
        # Se a solicitação for um POST, processe os dados do formulário
        form = FilmeForm(request.POST, request.FILES, instance=filme)
        if form.is_valid():
            form.save()
            return redirect("atualizar", id=id)  # Redirecione para a página de atualização
    else:
        # Se a solicitação não for um POST, exiba o formulário preenchido com os dados do filme
        form = FilmeForm(instance=filme)

    # Renderize a página de atualização com o formulário e o filme correspondente
    return render(request, 'atualizar.html', {'form': form, 'filme': filme})



def detalhar(request, id):
    filme = Filme.objects.get(id=id)
    return render(request, 'detalhar.html', {'filme':filme})


def deletar(request, id):
    filme = Filme.objects.get(id=id)
    filme.delete()
    return redirect('listar')
