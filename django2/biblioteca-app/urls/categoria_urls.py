
from django.urls import path
from catalogo.views.categoria_view import (categoria_list, 
                                    categoria_create, 
                                    categoria_update, 
                                    categoria_delete,)  

urlpatterns = [
    path('', 
        categoria_list, 
        name='categoria_list'),
    path('crear/', 
        categoria_create, 
        name='categoria_create'),
    path('editar/<int:pk>/', 
        categoria_update, 
        name='categoria_update'),
    path('eliminar/<int:pk>/', 
        categoria_delete, 
        name='categoria_delete'),
]
