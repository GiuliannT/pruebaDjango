from django.shortcuts import render, HttpResponse

# Create your views here.
def inicio(request):
    return HttpResponse("Pagina de inicio")

def saludar(request):
    variable = 5+7
    return HttpResponse(f"Hola mundo {variable}")
