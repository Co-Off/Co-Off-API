from rest_framework.serializers import ModelSerializer, SlugRelatedField
from core.models import Produto
from uploader.models import Image
from uploader.serializers import ImageSerializer

class ProdutoSerializer(ModelSerializer):
        capa_attachment_key = SlugRelatedField(
                source="imagem_do_produto",
                queryset=Image.objects.all(),
                slug_field="attachment_key",
                required=False,
                write_only=True,
        )
        imagemDoProduto = ImageSerializer(
                required=False,
                read_only=True
        )
        class Meta:
                model = Produto
                fields = "__all__"

class ProdutoDetailSerializer(ModelSerializer):
        imagemDoProduto = ImageSerializer(required=False)
        
class Meta:
        model = Produto
        fields = "__all__"
        depth = 1

class LivroListSerializer(ModelSerializer):
    class Meta:
        model = Produto
        fields = ("id", "titulo", "preco")