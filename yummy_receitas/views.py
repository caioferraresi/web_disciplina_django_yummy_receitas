from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from .models import Categoria
from .forms import ReceitaForm


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