from django.db import models
import os
from .managers import ReceitaManager


class Categoria(models.Model):
    nome = models.CharField(max_length=200, null=True)

    class Meta:
        verbose_name = 'categoria'

    def __str__(self):
        return self.nome

    def __str__(self):
        """Return a string representation of the model."""
        return self.nome


class Receita(models.Model):
    date_added = models.DateTimeField(auto_now_add=True)
    nome = models.CharField(max_length=200, null=True)
    autor = models.CharField(max_length=200, null=True)
    descricao = models.TextField()
    imagem = models.CharField(max_length=200, null=True)
    video = models.CharField(max_length=200, null=False)
    categoria = models.ManyToManyField('Categoria', through='CategoryMember', related_name='categorias')
    ingredientes = models.ManyToManyField('Ingrediente', through='IngredientDetail', related_name='ingredientes')
    tempo_preparo = models.CharField(max_length=10, null=True)
    instrucoes_preparo = models.TextField(null=True)
    porcoes = models.CharField(max_length=200, null=True)
    valor_nutricional = models.TextField(null=True)
    metodo_cozimento = models.CharField(max_length=200, null=True)

    objects = ReceitaManager()

    class Meta:
        verbose_name = 'receita'

    def __str__(self):
        """Return a string representation of the model."""
        return self.nome


class Ingrediente(models.Model):
    date_added = models.DateTimeField(auto_now_add=True)
    nome = models.CharField(max_length=200, null=True)

    class Meta:
        verbose_name = 'ingrediente'

    def __str__(self):
        """Return a string representation of the model."""
        return self.nome


class CategoryMember(models.Model):
    receita = models.ForeignKey(Receita, related_name='membershipCategoria')
    categoria = models.ForeignKey(Categoria, related_name='membershipCategoria')

    def __str__(self):
        return "%s está na categoria %s" % (self.receita, self.categoria)


class IngredientDetail(models.Model):
    receita = models.ForeignKey(Receita, related_name='membershipReceita')
    ingrediente = models.ForeignKey(Ingrediente, related_name='membershipReceita')
    quantidade = models.CharField(max_length=200, null=True)
    unidade = models.CharField(max_length=200, null=True)

    def __str__(self):
        return "%s está na receita %s" % (self.ingrediente, self.receita)
