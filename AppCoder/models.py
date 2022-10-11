from django.db import models
from requests import post

# Create your models here.


class Estudiante(models.Model):
    nombre = models.CharField(max_length=30, )
    apellido = models.CharField(max_length=30)
    cumpleaños = models.DateField()
    edad = models.IntegerField()
    profesion = models.CharField(max_length=30)

    def __str__(self):
       return f"{self.nombre}, {self.apellido} - {self.edad} - {self.profesion} - {self.cumpleaños}"    
    
    
class Profesor(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    profesion = models.CharField(max_length=30)

    def __str__(self):
       return f"{self.nombre}, {self.apellido} - {self.profesion}"


class Curso(models.Model):
    nombre = models.CharField(max_length=30)
    profesor = models.CharField(max_length=30)
    comision = models.IntegerField()

    def __str__(self):
       return f"({self.comision}) - {self.nombre}, {self.profesor}"    
