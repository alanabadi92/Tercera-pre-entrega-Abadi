from django.shortcuts import render
from app.forms import FormularioUsuario, FormularioPosteo
from app.models import Usuario, Posteo

def bienvenida(request):
    return render(request, 'bienvenida.html')

def ingresar_usuario(request):
    

    if (request.method == 'POST'):
        formulario = FormularioUsuario(request.POST)

        if formulario.is_valid():
            info= formulario.cleaned_data
            Usuario(nombre_usuario=info['nombre_usuario'], nombre_completo=info['nombre_completo'], email=info['email'], contrasena=info['contrasena'], genero=info['genero'],edad=info['edad']).save()
            print("se guardo usuario con exito")
            return render(request, 'exito.html', {"info":info})
            
    else:
        formulario = FormularioUsuario()

    return render(request, 'ingresar_usuario.html', {'formulario': formulario})

def hacer_posteo(request):

    if request.method == "POST":
        formulario = FormularioPosteo(request.POST)

        if formulario.is_valid():
            info = formulario.cleaned_data
            Posteo(titulo=formulario["titulo"], imagen=formulario["imagen"], descripcion=formulario["descripcion"]).save()
            return render(request, 'exito2.html', {"info":info})
    else:
        formulario = FormularioPosteo()

    return render(request, 'hacer_posteo.html', {'formulario': formulario})