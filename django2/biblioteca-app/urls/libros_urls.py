from django.urls import path
from catalogo.views.libro_view import libro_delete, libro_list, libro_create, libro_update

urlpatterns = [
    path('libros/', 
        libro_list, 
        name='libro_list'),
    path('libros/create/', 
        libro_create, 
        name='libro_create'),
    path('libros/update/<int:pk>/', 
        libro_update, 
        name='libro_update'),
    path('libros/delete/<int:pk>/', 
        libro_delete, 
        name='libro_delete'),
]