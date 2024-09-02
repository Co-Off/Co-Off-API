from django.db import models
from .categoria import Categoria
from .ingredientes import Ingrediente

class Produto(models.Model):
    nome = models.CharField(max_length=100)
    descrição = models.CharField(max_length=200)
    preco = models.DecimalField(max_digits=7, decimal_places=2, default=0, null=True, blank=True)
    categoria = models.ManyToManyField(Categoria, related_name="produtos", null=False, blank=True)
    ingredientes = models.ManyToManyField(Ingrediente, related_name="produtos", null=True, blank=True)
    quantidade = models.IntegerField(default=0, null=True, blank=True)

    def __str__(self):
        return self.nome
