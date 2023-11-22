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


class Movie(models.Model):

    CATEGORIAS = [
        ("comédia", "romance"),
        ("ação ", "aventura"),
        ("anime", "stand up"),
        
    ]

    titulo = models.CharField("Titulo", max_length=200)
    conteudo = models.TextField("Conteúdo")
    data_pub = models.DateField("Data de publicação")
    tags = models.CharField("Categoria", max_length=100, choices=CATEGORIAS)
    autor = models.ForeignKey(Filme, verbose_name="Filme", on_delete=models.CASCADE)

    def __str__(self):
        return self.titulo
    
    class Meta:
        verbose_name = "Movie"
        verbose_name_plural = "Movies"