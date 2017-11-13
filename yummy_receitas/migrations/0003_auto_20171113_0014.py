# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-13 00:14
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('yummy_receitas', '0002_auto_20171113_0008'),
    ]

    operations = [
        migrations.CreateModel(
            name='MetodoCozimento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=200, null=True)),
                ('date_added', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'metodocozimento',
            },
        ),
        migrations.AlterField(
            model_name='receita',
            name='metodo_cozimento',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, to='yummy_receitas.MetodoCozimento'),
            preserve_default=False,
        ),
    ]