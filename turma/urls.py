from django.urls import path
from . import views

app_name = 'turma'

urlpatterns = [
    path("lista", views.listar, name="listar"),
    path("cadastro", views.cadastrar, name="cadastrar"),
    path("registroAusencia", views.registroAusencia, name="registroAusencia"),
   
]