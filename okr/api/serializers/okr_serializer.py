from rest_framework import serializers
from okr.models import Okr, Integrante


class OkrSerializer(serializers.ModelSerializer):
    integrante_nome = serializers.StringRelatedField(source='integrante.nome')
    class Meta:
        model = Okr
        fields = ('id', 'integrante', 'integrante_nome', 'objetivo', 'resultado_1', 'resultado_2',
                  'resultado_3', 'resultado_4', 'resultado_5', 'criado', 'atualizado')

