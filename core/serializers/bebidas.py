from rest_framework.serializers import ModelSerializer

from core.models import Bebida

class BebidaSerializer(ModelSerializer):
    class Meta:
        model = Bebida
        fields = "__all__"