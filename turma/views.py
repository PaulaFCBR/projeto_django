from django.shortcuts import render

# Create your views here.
def listar(request):
    return render(request, 'turma/listarTurmas.html')

def cadastrar(request):
    return render(request, 'turma/cadastroTurma.html')

def registroAusencia(request):
    return render(request, 'turma/registroAusencia.html')