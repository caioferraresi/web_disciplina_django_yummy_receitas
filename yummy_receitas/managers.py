from django.db import models

class ReceitaManager(models.Manager):
    def create_receita(self, date_added, nome, autor, descricao, imagem, video, tempo_preparo, instrucoes_preparo, porcoes, valor_nutricional, metodo_cozimento):
        receita = self.create(date_added=date_added, nome=nome, autor=autor, descricao=descricao, imagem=imagem, video=video, tempo_preparo=tempo_preparo, instrucoes_preparo=instrucoes_preparo, porcoes=porcoes, valor_nutricional=valor_nutricional, metodo_cozimento=metodo_cozimento)
        return receita