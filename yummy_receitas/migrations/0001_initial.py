# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-12-05 04:17
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import yummy_receitas.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=200, null=True)),
                ('date_added', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'categoria',
            },
        ),
        migrations.CreateModel(
            name='Receita',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('nome', models.CharField(max_length=200, null=True)),
                ('autor', models.CharField(max_length=200, null=True)),
                ('descricao', models.TextField()),
                ('imagem', models.ImageField(blank=True, null=True, upload_to=yummy_receitas.models.get_image_path)),
                ('video', models.ImageField(blank=True, null=True, upload_to=yummy_receitas.models.get_image_path)),
                ('ingredientes', models.TextField(null=True)),
                ('tempo_preparo', models.CharField(max_length=200, null=True)),
                ('instrucoes_preparo', models.TextField(null=True)),
                ('porcoes', models.CharField(max_length=200, null=True)),
                ('valor_nutricional', models.TextField(null=True)),
                ('metodo_cozimento', models.CharField(max_length=200, null=True)),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='receitas', to='yummy_receitas.Categoria')),
            ],
            options={
                'verbose_name': 'receita',
            },
        ),
    ]
