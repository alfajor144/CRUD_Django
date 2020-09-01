from django.urls import path
from .views import crearPersona, listarPersona,editarPersona, eliminarPersona

urlpatterns = [
    path('crearPersona/', crearPersona, name = 'crearPersona'),
    path('editarPersona/<int:id>', editarPersona, name = 'editarPersona'),
    path('listarPersona/',listarPersona,name = 'listarPersona'),
    path('eliminarPersona/<int:id>',eliminarPersona, name = 'eliminarPersona')
]