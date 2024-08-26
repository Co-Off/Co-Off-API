from django.db import models
from .bebidas import Bebida
from .comidas import Comida
from .user import User

class Compra(models.Model):
    class StatusCompra(models.IntegerChoices):
        CARRINHO = 1, "Carrinho"
        REALIZADO = 2, "Realizado"
        PAGO = 3, "Pago"
        ENTREGUE = 4, "Entregue"

    usuario = models.ForeignKey(User, on_delete=models.PROTECT, related_name="compras")
    status = models.IntegerField(choices=StatusCompra.choices,  default=StatusCompra.CARRINHO)

    class ItensCompra(models.Model):
     compra = models.ForeignKey(Compra, on_delete=models.CASCADE, related_name="itens")
     bebida = models.ForeignKey(Bebida, on_delete=models.PROTECT, related_name="+")
     comida = models.ForeignKey(Comida, on_delete=models.PROTECT, related_name="+")
     quantidade = models.IntegerField(default=1)