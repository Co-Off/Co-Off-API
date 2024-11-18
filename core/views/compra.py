from core.models import Compra
from django.db import transaction
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.viewsets import ModelViewSet
from core.serializers import CompraSerializer, CompraCreateUpdateSerializer


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
                if item.quantidade > item.livro.quantidade:
                    return Response(
                        status=status.HTTP_400_BAD_REQUEST,
                        data={
                            "status": "Quantidade insuficiente",
                            "livro": item.livro.titulo,
                            "quantidade_disponivel": item.livro.quantidade,
                        },
                    )

                item.livro.quantidade -= item.quantidade
                item.livro.save()
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

    def get_serializer_class(self):
        if self.action in ("create", "update"):
            return CompraCreateUpdateSerializer
        return CompraSerializer
