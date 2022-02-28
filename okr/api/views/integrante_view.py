from rest_framework import viewsets
from okr.api.serializers.integrante_serializer import IntegranteSerializer
from okr.models import Integrante


class IntegranteViewSet(viewsets.ModelViewSet):

    queryset = Integrante.objects.all()
    serializer_class = IntegranteSerializer


