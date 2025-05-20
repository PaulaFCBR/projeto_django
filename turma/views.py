from django.shortcuts import HttpResponse

# Create your views here.
def exibe_mensagem(request):
    t_html = '<html><body>Turma!</body></html>'
    return HttpResponse(t_html)