from django.shortcuts import render
from AppBootcamps.views import *

# Create your views here.
def inicio(request):
    return render(request, "AppBootcamps/inicio.html")


def cursos(request):
    return render(request, "AppBootcamps/cursos.html")


def entregables(request):
    return render(request, "AppBootcamps/entregables.html")


def estudiantes(request):
    return render(request, "AppBootcamps/estudiantes.html")


def profesores(request):
    return render(request, "AppBootcamps/profesores.html")