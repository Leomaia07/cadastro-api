from rest_framework import viewsets

from .models import cadastro
from .serializers import CadastroSerializer

class cadastroViewSet(viewsets.ModelViewSet):
    queryset = cadastro.objects.all()
    serializer_class = CadastroSerializer