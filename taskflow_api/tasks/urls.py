# tasks/urls.py
from django.urls import path
from . import views


app_name = "tasks"   # namespace de la app — ver nota más abajo

urlpatterns = [
    path("", views.Home, name="home"),
    path("register", views.register, name="register"),
    path("presentacion", views.presentacion, name="presentacion"),
    path("saludo/<str:nombre>", views.greeting, name="saludo"),
    path("destinatario/<str:titulo>/<str:nombre>/<str:cargo>", 
        views.destination, name="destinatario"),
    path("area-triangulo/<int:base>/<int:altura>", 
        views.area_triangulo, name="area-triangulo"),
    path("my-first-template", views.my_first_template, 
        name="my-first-template"),
    path("tasks/projects", views.project_list, name="projects"),
    path("projects/new/", views.project_create, name="project_create"),
    path("projects/<int:pk>/edit/", views.project_edit, name="project_edit"),
    path("tasks/new/", views.task_create, name="task_create"),
    path("tasks/<int:pk>/edit/", views.task_edit, name="task_edit"),
]   