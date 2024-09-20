from django import forms

class FormularioUsuario(forms.Form):
    nombre = forms.CharField()
    apellido = forms.CharField(max_length=80)
    email = forms.EmailField()
    contrasena = forms.CharField(max_length=80)
    genero = forms.CharField(max_length=80)
    edad = forms.IntegerField()