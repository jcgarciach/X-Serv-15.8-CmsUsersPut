from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse, HttpResponseNotFound
from django.views.decorators.csrf import csrf_exempt

from .models import Pages

FORMULARIO = """
    <form action= "/" Method= "POST">
    URL:<br>
    <input type="text" name="name"><br>
    <input type="text" name="page"><br>
    <input type="submit" value="Enviar">
</form>
"""

def barra(request):

    lista = Pages.objects.all()
    respuesta = "<ul>"
    for pag in lista:
        respuesta += '<li><a href = "/pages/' + str(pag.id) + '">' + pag.name + ">/a>"
    respuesta += "</ul>"
    if request.user.is_authenticated():
        logged = 'Logged in' + request.user.username + '<br><a href="/logout">Logout</a>'
        repuesta = "<html><body><h1>" + logged + FORMULARIO + "</h1><p>" + respuesta + "</p></body></html>"
    else:
        logged = 'Not logged in' + '<a href="/login">Login</a>'
        respuesta = "<html><body><h1>" + logged + "</h1><p>" + respuesta + "</p></body></html>"
           
    return HttpResponse (respuesta)

@csrf_exempt
     
def pages(request, num):
    if request.method == "POST":
        page = Pages(name = request.POST['name'], page = request.POST['page'])
        page.save()
        
    try:
        page = Pages.objects.get(id = str(num))
    except Pages.DoesNotExist:
        return HttpResponseNotFound ('<h1>' + num + 'Not Found </h1>')
    return HttpResponse(page.name + " " + str(page.page))
