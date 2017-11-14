from django.conf.urls import url
from . import views

urlpatterns = [
    #home page
    url(r'^$', views.inicial, name='inicial'),

    #exibir todas as categorias
    url(r'^categorias/$', views.categorias, name='categorias'),

    #detalhe de cada categoria
    url(r'^categoria/(?P<categoria_id>\d+)/$', views.categoria, name='categoria'),

]