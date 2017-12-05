from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from .models import Categoria
from .forms import ReceitaForm

from .models import Receita
from rest_framework import viewsets
from rest_framework.decorators import detail_route, list_route
from .serializers import ReceitaSerializer
import datetime



class ReceitaViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Receita.objects.all()
    serializer_class = ReceitaSerializer


    def list(self, request):
        pass

    def create(self, request):
        date_added = datetime.datetime.now()
        nome = request.POST['nomeReceita']
        autor = user.email
        descricao = request.POST['descricao']
        imagem = request.POST['imagemReceita']
        video = request.POST['videoReceita']
        tempo_preparo = request.POST['tempoPreparo']
        instrucoes_preparo = request.POST['instrucoesPreparo']
        porcoes = request.POST['porcoes']
        valor_nutricional = request.POST['valorNutricional']
        metodo_cozimento = request.POST['metodoCozimento']
        
        receita = Receita.objects.create_receita(self, date_added, nome, autor, descricao, imagem, video, tempo_preparo, instrucoes_preparo, porcoes, valor_nutricional, metodo_cozimento)
        receita.save()


# Create your views here.
def inicial(request):
    return render(request, 'inicial.html')


def categorias(request):
    categorias = Categoria.objects.order_by('date_added')
    context = {'categorias': categorias}
    return render(request, 'categorias.html', context)


def categoria(request, categoria_id):
    """Show a single category and all its entries."""
    categoria = Categoria.objects.get(id=categoria_id)
    receitas = categoria.receitas.order_by('-date_added')
    context = {'categoria': categoria, 'receitas': receitas}
    return render(request, 'categoria.html', context)

def nova_receita(request, categoria_id):
    categoria = Categoria.objects.get(id=categoria_id)
    if request.method != 'POST':
        form = ReceitaForm()
    else:
        form = ReceitaForm(data=request.POST)
        if form.is_valid():
            nova_receita = form.save(commit=False)
            nova_receita.categoria = categoria
            nova_receita.save()
            return HttpResponseRedirect(reverse('yummy_receitas:categoria', args=[categoria_id]))

    context = {'categoria': categoria, 'form': form}
    return render(request, 'nova_receita.html', context)


