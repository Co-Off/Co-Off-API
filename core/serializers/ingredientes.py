from rest_framework.serializers import ModelSerializer

from core.models import Ingrediente

class IngredienteSerializer(ModelSerializer):
    class Meta:
        model = Ingrediente
        fields = "__all__"