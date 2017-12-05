from django.contrib import admin
from yummy_receitas.models import Receita, Categoria, Ingrediente, CategoryMember, IngredientDetail

# Register your models here.

admin.site.register(Receita)
admin.site.register(Categoria)
admin.site.register(Ingrediente)
admin.site.register(CategoryMember)
admin.site.register(IngredientDetail)
