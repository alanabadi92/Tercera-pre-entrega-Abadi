from django import forms

class FormularioUsuario(forms.Form):
    nombre_usuario = forms.CharField()
    nombre_completo = forms.CharField(max_length=80)
    email = forms.EmailField()
    contrasena = forms.CharField(max_length=80)
    genero = forms.CharField(max_length=80)
    edad = forms.IntegerField()

class FormularioPosteo(forms.Form):
    titulo = forms.CharField()
    imagen = forms.ImageField()
    descripcion = forms.CharField()
