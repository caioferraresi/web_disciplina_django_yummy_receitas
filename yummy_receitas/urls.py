from django.conf.urls import url, include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'receitas', views.ReceitaViewSet)


urlpatterns = [
    url(r'^', include(router.urls)),


    #home page
    url(r'^$', views.inicial, name='inicial'),

    #exibir todas as categorias
    url(r'^categorias/$', views.categorias, name='categorias'),

    #detalhe de cada categoria
    url(r'^categoria/(?P<categoria_id>\d+)/$', views.categoria, name='categoria'),

    # Página para adicionar nova receita
    url(r'^nova_receita/(?P<categoria_id>\d+)/$', views.nova_receita, name='nova_receita'),
]