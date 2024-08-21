from rest_framework.viewsets import ModelViewSet

from core.models import Bebida
from core.serializers import BebidaSerializer

class BebidaViewSet(ModelViewSet):
    queryset = Bebida.objects.all()
    serializer_class = BebidaSerializer