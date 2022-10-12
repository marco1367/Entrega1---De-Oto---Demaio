from django.urls import path
from AppBootcamps.views import *


urlpatterns = [
    path('', inicio, name="Inicio"),
    path('cursos', cursos, name="Cursos"),
    path('entregables', entregables, name="Entregables"),
    path('estudiantes', estudiantes, name="Estudiantes"),
    path('profesores', profesores, name="Profesores"),
]