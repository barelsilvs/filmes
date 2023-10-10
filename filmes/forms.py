from django.forms import ModelForm
from .models import Filme

class FilmeForm(ModelForm):
   
    class Meta:
        model=Filme
        fields='__all__'