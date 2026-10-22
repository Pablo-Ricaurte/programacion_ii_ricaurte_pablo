from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse

# Create your views here.
def home(request):
    """Vista de bienvenidad de la app tasks"""
    url_about = reverse("tasks:about")
    return HttpResponse(f"La URL de la pagina About es: {url_about}")
    # return HttpResponse(f"Hola, TaskFlow (método: {request.method})")


def about(request):
    return HttpResponse("TaskFlow - gestor de tareas y proyectos")

def saludo(request, nombre):
    return HttpResponse(f"hola, {nombre}")

def sumar(request, a, b):
    return HttpResponse(f"{a} + {b} = {a + b}")