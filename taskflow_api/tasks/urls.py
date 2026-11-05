from django.urls import path
from . import views

app_name = "tasks"

urlpatterns = [
    path('', views.home, name='home'),
    path('pacientes/', views.lista_pacientes, name='lista_pacientes'),
    path('planes/crear/', views.crear_plan_dietetico, name='crear_plan_dietetico'),
]