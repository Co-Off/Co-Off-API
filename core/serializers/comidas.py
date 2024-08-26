from rest_framework.serializers import ModelSerializer

from core.models import Comida

class ComidaSerializer(ModelSerializer):
    class Meta:
        model = Comida
        fields = "__all__"