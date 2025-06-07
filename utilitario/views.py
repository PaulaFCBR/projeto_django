from django.shortcuts import render, redirect
from utilitario import utils

# Create your views here.

def cadastrar(request):
    return render(request, 'utilitario/contato.html')

def popular_bd(request):
    utils.truncar_tabelas()
    utils.popular_tiposdeatividade()
    utils.popular_titulo()
    utils.popular_aluno()
    utils.popular_instrutor()
    utils.popular_turma()

    return redirect('/')
    
