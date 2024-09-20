from django.shortcuts import render
from app.forms import FormularioUsuario
from app.models import Usuario

def bienvenida(request):
    return render(request, 'bienvenida.html')

def ingresar_usuario(request):
    

    if (request.method == 'POST'):
        formulario = FormularioUsuario(request.POST)

        if formulario.is_valid():
            info= formulario.cleaned_data
            Usuario(nombre=info['nombre'], apellido=info['apellido'], email=info['email'], contrasena=info['contrasena'], genero=info['genero'],edad=info['edad']).save()
            print("se guardo usuario con exito")
            
    else:
        formulario = FormularioUsuario()

    return render(request, 'ingresar_usuario.html', {'formulario': formulario})
