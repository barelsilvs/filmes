from django.urls import path
from . import views
from .views import detalhar, listar, cadastrar, atualizar, deletar

urlpatterns = [
    path('', listar, name='listar'),
    path('cadastrar/', cadastrar, name='cadastrar'),
    path('atualizar/<int:id>/', atualizar, name='atualizar'),
    path('<int:id>', detalhar, name='detalhar'),
    path('deletar/<int:id>', deletar, name='deletar')
    # Outras URLs da sua aplicação "filmes"
]

