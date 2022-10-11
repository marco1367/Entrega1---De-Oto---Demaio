from django import forms

class Formulario_Estudiantes(forms.Form):
    
    nombre = forms.CharField(max_length=30, widget=forms.TextInput(attrs={'placeholder': 'Nombre', 'style': 'width: 20vw;'}))
    apellido = forms.CharField(max_length=30, widget=forms.TextInput(attrs={'placeholder': 'Apellido', 'style': 'width: 20vw;'}))
    cumpleaños = forms.DateField(input_formats=['%d/%m/%Y','%d-%m-%Y' ],widget=forms.TextInput(attrs={'label':'Fecha de Nacimiento','placeholder': 'Fecha de nacimiento', 'style': 'width: 20vw;'}))
    edad = forms.IntegerField(widget=forms.TextInput(attrs={'placeholder': 'Edad', 'style': 'width: 20vw;'}))
    profesion = forms.CharField(max_length=30, widget=forms.TextInput(attrs={'placeholder': 'Profesion', 'style': 'width: 20vw;'}))


class Formulario_Profesores(forms.Form):
    nombre = forms.CharField(max_length=30, widget=forms.TextInput(attrs={'placeholder': 'Nombre', 'style': 'width: 20vw;'}))
    apellido = forms.CharField(max_length=30, widget=forms.TextInput(attrs={'placeholder': 'Apellido', 'style': 'width: 20vw;'}))
    profesion = forms.CharField(max_length=30, widget=forms.TextInput(attrs={'placeholder': 'Profesión', 'style': 'width: 20vw;'}))
    
class Formulario_Cursos(forms.Form):
    nombre = forms.CharField(max_length=30, widget=forms.TextInput(attrs={'placeholder': 'Nombre', 'style': 'width: 20vw;'}))
    profesor = forms.CharField(max_length=30, widget=forms.TextInput(attrs={'placeholder': 'Profesor', 'style': 'width: 20vw;'}))
    comision = forms.IntegerField(widget=forms.NumberInput(attrs={'placeholder': 'XXXX', 'style': 'width: 20vw;'}))
    
