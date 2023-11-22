from django.contrib import admin
from django.urls import path
from .views import FilmeListView, FilmeDetailView, FilmeCreateView, FilmeUpdateView, FilmeDeleteView, MovieListView, MovieDetailView, MovieCreateView, MovieDeleteView, MovieUpdateView

urlpatterns = [
    path('filme', FilmeListView.as_view(), name='listar-filme'),
    path('filme/<int:id>', FilmeDetailView.as_view(), name='detalhar-filme'),
    path('filme/cadastrar/', FilmeCreateView.as_view(), name='cadastrar-filme'),
    path('filme/atualizar/<int:id>', FilmeUpdateView.as_view(), name='atualizar-filme'),
    path('filme/deletar/<int:id>', FilmeDeleteView.as_view(), name='deletar-filme'),
    path('movie', MovieListView.as_view(), name='listar-movie'),
    path('movie/<int:pk>', MovieDetailView.as_view(), name='detalhar-movie'),
    path('movie/cadastrar/', MovieCreateView.as_view(), name='cadastrar-movie'),
    path('movie/atualizar/<int:pk>', MovieUpdateView.as_view(), name='atualizar-movie'),
    path('movie/deletar/<int:pk>', MovieDeleteView.as_view(), name='deletar-movie'),
    ]






