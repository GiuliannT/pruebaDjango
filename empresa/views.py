from django.shortcuts import render, HttpResponse

# Create your views here.
def inicio(request):
    contexto = {
        "nombre":"Axel",
        "apellido":"Conti",
        "numero":24
    }
    return render(request, "bienvenido/inicio.html", contexto)
    #return HttpResponse("<h1>Pagina de inicio<h1>")

def saludar(request):
    variable = 5+7
    return HttpResponse(f"Hola mundo {variable}")

def saludar2(request):
    variable = 4214124+414
    return HttpResponse(f"Hola mundosdada {variable}")