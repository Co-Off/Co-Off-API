from django.db import models
from .categoria import Categoria
from .ingredientes import Ingrediente

class Comida(models.Model):
    nome = models.CharField(max_length=100)
    descrição = models.CharField(max_length=200)
    preco = models.DecimalField(max_digits=7, decimal_places=2, default=0, null=True, blank=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.PROTECT, related_name="comidas", null=False, blank=True)
    ingredientes = models.ForeignKey(Ingrediente, on_delete=models.PROTECT, related_name="comidas", null=True, blank=True)
    quantidade = models.IntegerField(default=0, null=True, blank=True)

    def __str__(self):
        return self.nome