from django.shortcuts import render, redirect
from .models import Paciente, PlanDietetico
from .forms import PlanDieteticoForm

def home(request):
    return render(request, 'tasks/home.html')


def lista_pacientes(request):
    pacientes = Paciente.objects.all()
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