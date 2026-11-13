from django.urls import path
from catalogo.views.autor_views import (autor_list,
                                    autor_create,
                                    autor_update,
                                    autor_delete,)

urlpatterns = [
    path('autores/', autor_list, name='autor_list'),
    path('autores/create/', autor_create, name='autor_create'),
    path('autores/update/<int:pk>/', autor_update, name='autor_update'),
    path('autores/delete/<int:pk>/', autor_delete, name='autor_delete'),
]