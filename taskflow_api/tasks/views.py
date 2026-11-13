from django.shortcuts import render, redirect
from .models import Paciente, PlanDietetico
from .forms import PlanDieteticoForm

def home(request):
    return render(request, 'tasks/home.html')


def lista_pacientes(request):
    pacientes = Paciente.objfrom django.http import HttpResponse

from django.shortcuts import get_object_or_404, redirect, render
from .forms import ProjectForm, TaskForm
from .models import Project, Task

def Home(request):
    contexto = {
        "titulo": "TaskFlow",
        "mensaje": "Organiza tus proyectos y tareas en un solo lugar",
        "projects": Project.objects.order_by("-created_at"),
    }
    return render(request, "tasks/home.html", contexto)

def project_list(request):
    contexto = {
        "titulo": "TaskFlow",
        "mensaje": "Organiza tus proyectos y tareas en un solo lugar",
        "projects": Project.objects.order_by("-created_at"),
    }
    return render(request, "projects/projects.html", contexto)

def task_create(request):
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save()
            return redirect("tasks:home")
    else:
        form = TaskForm()

    return render(request, "tasks/task_form.html", {"form": form, "modo": "crear"})

def task_edit(request, pk):
    task = get_object_or_404(Task, pk=pk)

    if request.method == "POST":
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect("tasks:home")
    else:
        form = TaskForm(instance=task)

    return render(request, "tasks/task_form.html", {"form": form, "modo": "editar"})

def register(request):
    """Registros de usuarios"""
    return HttpResponse("Registros de Usuarios en línea")

def presentacion(request):
    """Presentacion del programador"""
    return HttpResponse("Si ves esta línea de código, es que hice algo y funcionó - mateo rogeron")

def greeting(request, nombre):
    """"Registro de usuarios"""
    return HttpResponse(
        f"Hola, {nombre}. Bienvenido a TaskFlow"
    )

def destination(request, titulo, nombre, cargo):
    """"Registro de usuarios"""
    return HttpResponse(
        f"Bienvenido,{titulo} {nombre}, su cargo es {cargo}"
    )

def area_triangulo(request, base, altura):
    """Calcula el área de un triángulo"""
    return HttpResponse(f"El área del triángulo es: {(base * altura) / 2}")

def my_first_template(request):
    contexto = {
        "titulo": "TaskFlow",
        "mensaje": "Organiza tus proyectos y tareas en un solo lugar",
    }
    return render(request, "tasks/my-first-template.html", contexto)

def leads_like(request):
    contexto = {
        "titulo": "Programador",
        "nombre": "Mateo Nicolay",
        "apellido": "Rogeron Maila",
    }
    return render(request, "leads/leads-like.html", contexto)

def project_create(request):
    if request.method == "POST":
        form = ProjectForm(request.POST)
        if form.is_valid():
            project = form.save()
            return redirect("tasks:projects")

    else:
        form = ProjectForm()

    return render(request, "projects/project_form.html", {"form": form, "modo": "crear"})

def project_edit(request, pk):
    project = get_object_or_404(Project, pk=pk)

    if request.method == "POST":
        form = ProjectForm(request.POST, instance=project)
        if form.is_valid():
            form.save()
            return redirect("tasks:projects")
    else:
        form = ProjectForm(instance=project)

    return render(request, "projects/project_form.html", {"form": form, "modo": "editar"})

ects.all()
    return render(request, 'tasks/pacientes.html', {'pacientes': pacientes})

def crear_plan_dietetico(request):
    if request.method == 'POST':
        form = PlanDieteticoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_pacientes')
    
    else:
        form = PlanDieteticoForm()
    return render(request, 'tasks/plan_form.html', {'form': form})