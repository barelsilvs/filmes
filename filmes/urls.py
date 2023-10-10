from django.urls import path
from . import views
from .views import detalhar, listar, cadastrar, atualizar

urlpatterns = [
    path('', views.home, name='home'),
    path('', listar, name='listar'),
    path('cadastrar/', cadastrar, name='cadastrar'),
    path('atualizar/<int:id>/', atualizar, name='atualizar'),
    path('<int:id>', detalhar, name='detalhar')
    # Outras URLs da sua aplicação "filmes"
]

