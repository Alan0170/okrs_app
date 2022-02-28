from rest_framework import serializers
from okr.models import Integrante, Okr


class IntegranteSerializer(serializers.ModelSerializer):

    class Meta:
        model = Integrante
        fields = ('id', 'nome', 'email')
