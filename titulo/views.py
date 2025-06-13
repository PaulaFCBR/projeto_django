from django.shortcuts import render, redirect
from titulo.models import Titulo
from titulo.forms import TituloForm, TituloAtualizarForm
from instrutor.models import Instrutor

# Create your views here.
def listar(request):
    lista_titulos = Titulo.objects.all()
    contexto = {
        'titulos' : lista_titulos
    }

    return render(request, 'titulo/listarTitulos.html',context=contexto)

def cadastro(request):
    return render(request, 'titulo/cadastroTitulos.html')

def cadastrar(request):
    form = TituloForm(request.POST)
    if form.is_valid():
        dados_titulo = form.cleaned_data
        titulo = Titulo(
            descricao = dados_titulo['descricao']
        )
        titulo.save()
    
    return render(request, 'titulo/cadastroTitulos.html')

def excluir(request, codigo):
    titulo = Titulo.objects.get(pk=codigo)
    instrutores = Instrutor.objects.filter(codigo_titulo=codigo)
    if not instrutores:
        titulo.delete()
    
    return redirect('titulo:listar')


def carregar_titulo(request, codigo):
    # obter titulo a atualizar baseado no codigo
    titulo = Titulo.objects.get(pk=codigo)
    contexto= {
        'titulo': titulo,
    }
    return render(request, 'titulo/atualizarTitulo.html', context = contexto)


def atualizar(request):
    if request.method == 'POST':
        form= TituloAtualizarForm(request.POST)
        if form.is_valid():
            dados_titulo =form.cleaned_data
            codigo = dados_titulo['codigo']
            titulo = Titulo.objects.get(pk=codigo)
            titulo.descricao = dados_titulo['descricao']

            titulo.save()
    return redirect('titulo:listar')        
        
