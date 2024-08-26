from rest_framework.viewsets import ModelViewSet

from core.models import Comida
from core.serializers import ComidaSerializer

class ComidaViewSet(ModelViewSet):
    queryset = Comida.objects.all()
    serializer_class = ComidaSerializer