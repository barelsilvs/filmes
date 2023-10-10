from django.db import models

# Create your models here.



from django.db import models

class Filme(models.Model):
    titulo = models.CharField(max_length=200)
    diretor = models.CharField(max_length=100)
    genero = models.CharField(max_length=50)
    sinopse = models.TextField()
    
    def __str__(self):
        return self.titulo
