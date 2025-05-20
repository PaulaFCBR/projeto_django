from django.shortcuts import HttpResponse, render

# Create your views here.
def exibe_mensagem(request):
    t_html = '<html><body>Utilitario</body></html>'
    return HttpResponse(t_html)