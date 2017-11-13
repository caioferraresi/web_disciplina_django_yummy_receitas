from django.db import models
import os


def get_image_path(instance, filename):
    return os.path.join('photos', str(instance.id), filename)


class Categoria(models.Model):

    nome = models.CharField(max_length=200, null=True)
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'categoria'

    def __str__(self):
        """Return a string representation of the model."""
        return self.nome


class Receita(models.Model):

    date_added = models.DateTimeField(auto_now_add=True)
    nome = models.CharField(max_length=200, null=True)

    autor = models.CharField(max_length=200, null=True)
    descricao = models.TextField()
    imagem = models.ImageField(upload_to=get_image_path, blank=True, null=True)
    video = models.ImageField(upload_to=get_image_path, blank=True, null=True)

    #chave classe Categoria
    categoria = models.ForeignKey(Categoria)

    ingredientes = models.TextField(null=True)
    tempo_preparo = models.CharField(max_length=200, null=True)
    instrucoes_preparo = models.TextField(null=True)
    porcoes = models.CharField(max_length=200, null=True)
    valor_nutricional = models.TextField(null=True)
    metodo_cozimento = models.CharField(max_length=200, null=True)

    class Meta:
        verbose_name = 'receita'

    def __str__(self):
        """Return a string representation of the model."""
        return self.nome
