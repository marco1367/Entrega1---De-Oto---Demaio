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
        print(miFormulario)
        if miFormulario.is_valid:
            info = miFormulario.cleaned_data
            curso = Curso(nombre=info['nombre'], camada=info['camada'])
            curso.save()
            return render(request, "AppBootcamps/inicio.html")
    else:
        miFormulario = CursoFormulario()
    return render(request, "AppBootcamps/cursos.html", {"miFormulario": miFormulario})




def entregables(request):
    return render(request, "AppBootcamps/entregables.html")




def estudiantes(request):
    return render(request, "AppBootcamps/estudiantes.html")




def profesores(request):
    return render(request, "AppBootcamps/profesores.html")