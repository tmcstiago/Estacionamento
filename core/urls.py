from django.contrib import admin
from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.home, name='core_home'),

    path('pessoas/', views.lista_pessoas, name='core_lista_pessoas'),
    path('pessoa-novo/', views.pessoa_novo, name='core_pessoa_novo'),
    re_path(r'^pessoa-update/(?P<id>\d+)/$', views.pessoa_update, name='core_update_pessoa'),
    re_path(r'^pessoa-delete/(?P<id>\d+)/$', views.pessoa_delete, name='core_delete_pessoa'),

    path('veiculos/', views.lista_veiculos, name='core_lista_veiculos'),
    path('veiculo-novo', views.veiculo_novo, name='core_veiculo_novo'),
    re_path(r'^veiculo-update/(?P<id>\d+)/$', views.veiculo_update, name='core_veiculo_update'),

    path('mov-rot/', views.lista_mov_rotativos, name='core_lista_mov_rotativos'),
    path('mov-rot-novo/', views.mov_rotativo_novo, name = 'core_mov_rotativo_novo'),

    path('mensalistas/', views.lista_mensalistas, name='core_lista_mensalistas'),
    path('mensalista-novo/', views.mensalista_novo, name='core_mensalista_novo'),
    
    path('mov-mensalistas/', views.lista_mov_mensalistas, name='core_lista_mov_mensalistas'),
    path('mov-mensalista-novo/', views.mov_mensalista_novo, name = 'core_mov_mensalista_novo')
]