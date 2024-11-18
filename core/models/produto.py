from django.db import models
from .categoria import Categoria
from .ingrediente import Ingrediente
from uploader.models import Image


class Produto(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.CharField(max_length=200)
    preco = models.DecimalField(max_digits=7, decimal_places=2, default=0, null=True, blank=True)
    categoria = models.ManyToManyField(Categoria, related_name="produtos", blank=True)
    ingredientes = models.ManyToManyField(Ingrediente, related_name="produtos", blank=True)
    quantidade = models.IntegerField(default=0, null=True, blank=True)

    imagemDoProduto= models.ForeignKey(
        Image,
        related_name="+",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        default=None,
    )

    def __str__(self):
        return self.nome