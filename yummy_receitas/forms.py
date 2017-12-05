from django import forms
from .models import Receita


# class ReceitaForm(forms.ModelForm):

#     class Meta:
#         model = Receita

#         fields = ['nome', 'autor', 'descricao', 'imagem', 'video',
#                   'categoria','ingredientes','tempo_preparo',
#                   'instrucoes_preparo', 'porcoes', 'valor_nutricional', 'metodo_cozimento']
#       #  labels = {'text': ''}
#       #  widgets = {'text': forms.Textarea(attrs={'cols': 80})}