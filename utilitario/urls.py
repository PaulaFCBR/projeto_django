from django.urls import path
from . import views

app_name = 'utilitario'

urlpatterns = [
    path("cadastro", views.cadastrar, name="cadastrar"),
    
   
]