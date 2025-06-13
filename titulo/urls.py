from django.urls import path
from . import views

app_name = 'titulo'

urlpatterns = [
    path("lista/", views.listar, name="listar"),
    path("cadastro/", views.cadastro, name="cadastro"),
    path("cadastrar/", views.cadastrar, name="cadastrar"),
    path("excluir/<int:codigo>", views.excluir, name="excluir_titulo"),  
    path('carregar_titulo/<int:codigo>', views.carregar_titulo, name="carregar_titulo"),
    path('atualizar_Titulo/', views.atualizar, name='atualizar_titulo'),
]