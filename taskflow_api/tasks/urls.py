from django.urls import path
from . import views

app_name = "tasks"

urlpatterns = [
    path("", views.home, name="home"),
    path("about/", views.about, name="about"),
    path("saludo/<str:nombre>/", views.saludo, name="saludo"),
    path("sumar/<int:a>/<int:b>", views.sumar, name="sumar")
]