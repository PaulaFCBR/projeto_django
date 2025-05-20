from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("exibemensagem", views.exibe_mensagem, name="exibe_mensagem"),
    path('exibemensagensimples', views.exibe_html_simples, name="exibe_html_simples"),
    path("test_render", views.test_render,name="render_exibir"),
]