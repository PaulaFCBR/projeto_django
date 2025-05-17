from django.shortcuts import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("Olá eu sou index")

def exibe_mensagem(request):
    t_html = '<html><body>Hello</body></html>'
    return HttpResponse(t_html)