from core.models import Compra, ItensCompra
from rest_framework.serializers import CharField, ModelSerializer, SerializerMethodField

class ItensCompraSerializer(ModelSerializer):
    total = SerializerMethodField()

    def get_total(self, instance):
        return instance.produto.preco * instance.quantidade

    class Meta:
        model = ItensCompra
        fields = ("produto", "quantidade", "total")
        depth = 1

class CompraSerializer(ModelSerializer):
        usuario = CharField(source="usuario.email", read_only=True)
        status = CharField(source="get_status_display", read_only=True)
        itens = ItensCompraSerializer(many=True, read_only=True)

        class Meta:
            model = Compra
            fields = ("id", "usuario", "status", "itens")
            depth = 1

class CriarEditarItensCompraSerializer(ModelSerializer):
    class Meta:
        model = ItensCompra
        fields = ("produto", "quantidade")

class CriarEditarCompraSerializer(ModelSerializer):
    itens = CriarEditarItensCompraSerializer(many=True)

    class Meta:
        model = Compra
        fields = ("usuario", "itens")

    def create(self, validated_data):
        itens_data = validated_data.pop("itens")
        compra = Compra.objects.create(**validated_data)
        for item_data in itens_data:
            ItensCompra.objects.create(compra=compra, **item_data)
        compra.save()
        return compra
    
class ListarItensCompraSerializer(ModelSerializer):
    produto = CharField(source="produto.nome", read_only=True)

    class Meta:
        model = ItensCompra
        fields = ("quantidade", "produto")
        depth = 1

class ListarCompraSerializer(ModelSerializer):
    usuario = CharField(source="usuario.email", read_only=True)
    itens = ListarItensCompraSerializer(many=True, read_only=True)

    class Meta:
        model = Compra
        fields = ("id", "usuario", "itens")
