from django.db import models
from .categoria import Categoria
from .autor import Autor

class Libro(models.Model):
    titulo = models.CharField(max_length=200)
    fecha_publicacion = models.DateField()
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    isbn = models.CharField(max_length=100, unique=True)
    autores = models.ManyToManyField(Autor, 
            related_name='libros',
            blank=True)

    def __str__(self):
        return self.titulo

    class Meta:
        verbose_name = "Libro"
        verbose_name_plural = "Libros"
        ordering = ['titulo']
