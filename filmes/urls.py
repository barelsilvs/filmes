from django.urls import path
from . import views
from .views import detalhar, listar, cadastrar, atualizar, deletar, MovieListView, MovieDetailView, MovieCreateView, MovieUpdateView, MovieDeleteView

urlpatterns = [
    path('', listar, name='listar'),
    path('cadastrar/', cadastrar, name='cadastrar'),
    path('atualizar/<int:id>/', atualizar, name='atualizar'),
    path('<int:id>', detalhar, name='detalhar'),
    path('deletar/<int:id>', deletar, name='deletar'),
    path('movie', MovieListView.as_view(), name='listar-movie'),
    path('movie/<int:pk>', MovieDetailView.as_view(), name='detalhar-movie'),
    path('movie/cadastrar/', MovieCreateView.as_view(), name='cadastrar-movie'),
    path('movie/atualizar/<int:pk>', MovieUpdateView.as_view(), name='atualizar-movie'),
    path('movie/deletar/<int:pk>', MovieDeleteView.as_view(), name='deletar-movie'),
    # Outras URLs da sua aplicação "filmes"
]





