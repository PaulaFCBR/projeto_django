from django.urls import path

from . import views

urlpatterns = [
    path("exibemensagem", views.exibe_mensagem, name="exibe_mensagem"),
]