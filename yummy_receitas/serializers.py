from .models import Receita, Categoria, Ingrediente
from rest_framework import serializers


class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = ('nome',)


class IngredienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingrediente
        fields = ('nome',)


class ReceitaSerializer(serializers.ModelSerializer):
    categorias = CategoriaSerializer(many=True, read_only=True)
    ingredientes = IngredienteSerializer(many=True, read_only=True)
    
    class Meta:
        model = Receita
        fields = ('date_added', 'nome', 'autor', 'descricao', 'imagem',\
         'video', 'tempo_preparo', 'instrucoes_preparo', 'porcoes', 'valor_nutricional',\
         'metodo_cozimento',  'categorias', 'ingredientes')
