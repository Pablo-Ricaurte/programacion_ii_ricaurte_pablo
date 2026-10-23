from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse

# Create your views here.
def home(request):
    contexto = {
        "titulo": "Gestor de tareas",
        "mensaje": "Organiza tus proyectos y tareas en un solo lugar",
        "total_tareas": 7,
        "proyectos": [
            "Rediseño web",
            "Migracion de base de datos",
            "Documentacion API"
        ]
    }
    return render(request, "tasks/home.html", contexto)


def about(request):
    return render(request, "tasks/about.html")

def saludo(request, nombre):
    return HttpResponse(f"hola, {nombre}")

def sumar(request, a, b):
    return HttpResponse(f"{a} + {b} = {a + b}")