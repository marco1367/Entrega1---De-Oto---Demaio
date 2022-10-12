import imp
from django.shortcuts import render
from AppBootcamps.models import *
from AppBootcamps.forms import *

# Create your views here.
def inicio(request):
    return render(request, "AppBootcamps/inicio.html")



def cursos(request):
    if request.method == "POST":
        
        miFormulario = CursoFormulario(request.POST)
        if miFormulario.is_valid():
            info = miFormulario.cleaned_data
            curso = Curso(nombre=info['nombre'], camada=info['camada'])
            curso.save()
            return render(request, "AppBootcamps/inicio.html")
    else:
        miFormulario = CursoFormulario()
    return render(request, "AppBootcamps/cursos.html", {"miFormulario": miFormulario})




def entregables(request):
    if request.method == "POST":
        
        miFormulario = EntregablesFormulario(request.POST)
        if miFormulario.is_valid():
            info = miFormulario.cleaned_data
            curso = Entregable(nombre=info['nombre'], fechaDeEntrega=info['fechaDeEntrega'], entregado=info['entregado'])
            curso.save()
            return render(request, "AppBootcamps/inicio.html")
    else:
        miFormulario = EntregablesFormulario()
    return render(request, "AppBootcamps/entregables.html", {"miFormulario": miFormulario})
    # return render(request, "AppBootcamps/entregables.html")




def estudiantes(request):
    if request.method == "POST":
        
        miFormulario = EstudiantesFormulario(request.POST)
        if miFormulario.is_valid():
            info = miFormulario.cleaned_data
            curso = Estudiante(nombre=info['nombre'], apellido=info['apellido'], email=info['email'])
            curso.save()
            return render(request, "AppBootcamps/inicio.html")
    else:
        miFormulario = EstudiantesFormulario()
    return render(request, "AppBootcamps/estudiantes.html", {"miFormulario": miFormulario})
    # return render(request, "AppBootcamps/estudiantes.html")




def profesores(request):
    if request.method == "POST":
        
        miFormulario = ProfesoresFormulario(request.POST)
        if miFormulario.is_valid():
            info = miFormulario.cleaned_data
            curso = Profesor(nombre=info['nombre'], apellido=info['apellido'], email=info['email'], profesion=info['profesion'])
            curso.save()
            return render(request, "AppBootcamps/inicio.html")
    else:
        miFormulario = ProfesoresFormulario()
    return render(request, "AppBootcamps/profesores.html", {"miFormulario": miFormulario})
    # return render(request, "AppBootcamps/profesores.html")