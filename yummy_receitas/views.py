from django.shortcuts import render
from .models import Categoria


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