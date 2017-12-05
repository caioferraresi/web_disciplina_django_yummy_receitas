from .models import Receita
from rest_framework import serializers


class ReceitaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Receita
        fields = ('date_added', 'nome', 'autor', 'descricao', 'imagem', 'video', 'tempo_preparo', 'instrucoes_preparo', 'porcoes', 'valor_nutricional', 'metodo_cozimento')

