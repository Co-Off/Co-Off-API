from django.db import models


class Ingrediente(models.Model):
    descricao = models.CharField(max_length=100)

    def __str__(self):
        return self.descricao
    class StatusIngrediente(models.IntegerChoices):
        EM_ESTOQUE = 1, "Em Estoque"
        POUCAS_UNIDADES = 2, "Poucas Unidades"
        EM_FALTA = 3, "Em Falta"

    status = models.IntegerField(choices=StatusIngrediente.choices, default=StatusIngrediente.EM_ESTOQUE)