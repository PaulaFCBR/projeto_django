from django.shortcuts import HttpResponse, render

# Create your views here.
def index(request):
    return HttpResponse("Olá eu sou index")

def exibe_mensagem(request):
    t_html = '<html><body>Hello</body></html>'
    return HttpResponse(t_html)

def exibe_html_simples(request):
    t_html = '<html><body>Hello</body></html>'
    return HttpResponse(t_html)

def test_render(request):
    return render(request, 'escola.html')    
