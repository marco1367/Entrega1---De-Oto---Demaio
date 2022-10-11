from django.http import HttpResponse
from django.shortcuts import render
from AppCoder.forms import (
    Formulario_Estudiantes,
    Formulario_Profesores,
    Formulario_Cursos,
)
from AppCoder.models import Estudiante, Profesor, Curso


# Create your views here.
def show_home(request):
    return render(request, "AppCoder/home.html")


def estudiantes(request):
    return render(request, "AppCoder/estudiantes.html")


def procesar_formulario_estudiante(request):
    if request.method != "POST":
        mi_formulario = Formulario_Estudiantes()
        contexto = {"formulario": mi_formulario}
        return render(request, "AppCoder/formulario.html", context=contexto)
    
    else:
        mi_formulario = Formulario_Estudiantes(request.POST)
        if mi_formulario.is_valid():
            informacion = mi_formulario.cleaned_data
            nuevo_estudiante = Estudiante(
                nombre=informacion["nombre"],
                apellido=informacion["apellido"],
                cumpleaños=informacion["cumpleaños"],
                edad=informacion["edad"],
                profesion=informacion["profesion"],
            )
            nuevo_estudiante.save()
            return render(request, "AppCoder/home.html")
        
    contexto = {"formulario": mi_formulario}
    return render(request, "AppCoder/formulario.html", context=contexto)


def profesores(request):
    return render(request, "AppCoder/profesores.html")


def procesar_formulario_profesor(request):
    if request.method != "POST":
        mi_formulario = Formulario_Profesores()
        contexto = {"formulario": mi_formulario}
        return render(request, "AppCoder/formulario.html", context=contexto)
    
    else:
        mi_formulario = Formulario_Profesores(request.POST)
        if mi_formulario.is_valid():
            informacion = mi_formulario.cleaned_data
            nuevo_profesor = Profesor(
                nombre=informacion["nombre"],
                apellido=informacion["apellido"],
                profesion=informacion["profesion"],
            )
            nuevo_profesor.save()
            return render(request, "AppCoder/home.html")
        
    contexto = {"formulario": mi_formulario}
    return render(request, "AppCoder/formulario.html", context=contexto)


def cursos(request):
    return render(request, "AppCoder/cursos.html")


def procesar_formulario_curso(request):
    if request.method != "POST":
        mi_formulario = Formulario_Cursos()
        contexto = {"formulario": mi_formulario}
        return render(request, "AppCoder/formulario.html", context=contexto)
    
    else:
        mi_formulario = Formulario_Cursos(request.POST)
        if mi_formulario.is_valid():
            informacion = mi_formulario.cleaned_data
            nuevo_curso = Curso(
                nombre=informacion["nombre"],
                profesor=informacion["profesor"],
                comision=informacion["comision"],
            )
            nuevo_curso.save()
            return render(request, "AppCoder/home.html")
        
    contexto = {"formulario": mi_formulario}
    return render(request, "AppCoder/formulario.html", context=contexto)


def buscar(request):
    if request.method == "GET":
        return render(request, "AppCoder/busqueda.html")

    # if request.method == "POST":
    #     # Hacer algo con la base de datos
    #     comision_a_buscar = request.POST["comision"]
    #     resultados_de_busqueda = Curso.objects.filter(comision = comision_a_buscar)
    #     contexto = {"resultados": resultados_de_busqueda}
    #     return render(request, "AppCoder/resultado-busqueda.html", context=contexto)

 
def buscar(request):
    if request.method == "GET":
        return render(request, "AppCoder/busqueda.html")

    if request.method == "POST":
        # Hacer algo con la base de datos
        comision_a_buscar = request.POST["comision"]
        resultados_de_busqueda = Curso.objects.filter(comision = comision_a_buscar)
        contexto = {"resultados": resultados_de_busqueda}
        return render(request, "AppCoder/resultado-busqueda.html", context=contexto)

