from django import forms
from app.models import Usuario

class FormularioUsuario(forms.Form):
    nombre_usuario = forms.CharField()
    nombre_completo = forms.CharField(max_length=80)
    email = forms.EmailField()
    contrasena = forms.CharField(max_length=80)
    genero = forms.CharField(max_length=80)
    edad = forms.IntegerField()

class FormularioPosteo(forms.Form):
    titulo = forms.CharField(max_length=80, required=False)
    imagen = forms.ImageField(required=False)
    descripcion = forms.CharField(widget=forms.Textarea)
    usuario = forms.ModelChoiceField(queryset=Usuario.objects.all(), required=False)

class FormularioTest(forms.Form):
    usuario = forms.ModelChoiceField(queryset=Usuario.objects.all(), required=True)
    eneatipo = forms.IntegerField()
    energia2 = forms.IntegerField()
    energia3 = forms.IntegerField()


class FormularioBuscarUsuario(forms.Form):
    query = forms.CharField(label='Ingrese nombre de usuario', max_length=80)

