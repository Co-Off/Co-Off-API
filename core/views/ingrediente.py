from rest_framework.viewsets import ModelViewSet

from core.models import Ingrediente
from core.serializers import IngredienteSerializer

class IngredienteViewSet(ModelViewSet):
    queryset = Ingrediente.objects.all()
    serializer_class = IngredienteSerializer