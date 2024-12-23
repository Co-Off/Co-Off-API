from core.models import Compra
from django.db import transaction
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.viewsets import ModelViewSet
from core.serializers import CompraSerializer


class CompraViewSet(ModelViewSet):
    queryset = Compra.objects.all()
    serializer_class = CompraSerializer

    @action(detail=True, methods=["post"])
    def finalizar(self, request, pk=None):
        compra = self.get_object()
        if compra.status != Compra.StatusCompra.CARRINHO:
            return Response(
                status=status.HTTP_400_BAD_REQUEST,
                data={"status": "Compra já finalizada"},
            )
        with transaction.atomic():
            for item in compra.itens.all():
                if item.quantidade > item.produto.quantidade:
                    return Response(
                        status=status.HTTP_400_BAD_REQUEST,
                        data={
                            "status": "Quantidade insuficiente",
                            "produto": item.produto.titulo,
                            "quantidade_disponivel": item.produto.quantidade,
                        },
                    )

                item.produto.quantidade -= item.quantidade
                item.produto.save()
            compra.status = Compra.StatusCompra.REALIZADO
            compra.save()
        return Response(status=status.HTTP_200_OK, data={"status": "Compra finalizada"})

    @action(detail=False, methods=["get"])
    def relatorio_vendas_mes(self, request):
        agora = timezone.now()
        inicio_mes = agora.replace(day=1, hour=0, minute=0, second=0, microsecond=0)
        compras = Compra.objects.filter(status=Compra.StatusCompra.REALIZADO, data__gte=inicio_mes)
        total_vendas = sum(compra.total for compra in compras)
        quantidade_vendas = compras.count()

        return Response(
            {
                "status": "Relatório de vendas deste mês",
                "total_vendas": total_vendas,
                "quantidade_vendas": quantidade_vendas,
            },
            status=status.HTTP_200_OK,
        )
