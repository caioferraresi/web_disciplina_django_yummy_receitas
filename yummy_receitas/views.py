from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from .models import Categoria
# from .forms import ReceitaForm

from .models import Receita
from rest_framework import viewsets
from rest_framework.decorators import detail_route, list_route
from .serializers import ReceitaSerializer
from rest_framework.response import Response
import datetime



class ReceitaViewSet(viewsets.ModelViewSet):
    queryset = Receita.objects.all()
    serializer_class = ReceitaSerializer


    def list(self, request):
        receitas = Receita.objects.all()
        page = self.paginate_queryset(receitas)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)
        serializer = self.get_serializer(receitas, many=True)
        return Response(serializer.data)       


    def create(self, request):
        date_added = datetime.datetime.now()
        nome = request.data['nome']
        autor = "email"
        descricao = request.data['descricao']
        link_imagem = request.data['imagem']
        link_video = request.data['video']
        tempo_preparo = request.data['tempo_preparo']
        instrucoes_preparo = request.data['instrucoes_preparo']
        porcoes = request.data['porcoes']
        valor_nutricional = request.data['valor_nutricional']
        metodo_cozimento = request.data['metodo_cozimento']
        
        receita = Receita.objects.create_receita(date_added, nome, autor, descricao, link_imagem, link_video, tempo_preparo, instrucoes_preparo, porcoes, valor_nutricional, metodo_cozimento)
        receita.save()
        serializer = self.get_serializer(receita)
        return Response(serializer.data)


    def retrieve(self, request, pk=None):
        receitas = Receita.objects.get(pk=pk)
        serializer = self.get_serializer(receitas, many=True)
        return Response(serializer.data) 




