from django.forms import ModelForm
from .models import Filme, Movie

class FilmeForm(ModelForm):
   
    class Meta:
        model=Filme
        fields='__all__'

class MovieForm(ModelForm):
   
    class Meta:
        model=Movie
        fields='__all__'