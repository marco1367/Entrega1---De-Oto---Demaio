
from django.urls import path
from AppCoder.views import buscar, show_home, procesar_formulario_estudiante, procesar_formulario_curso, procesar_formulario_profesor
urlpatterns = [
    path('', show_home),
    path('home/', show_home),
    path('estudiantes/', procesar_formulario_estudiante),    
    path('profesores/', procesar_formulario_profesor),    
    path('cursos/', procesar_formulario_curso),    
    path('buscar/', buscar),    
    
]

