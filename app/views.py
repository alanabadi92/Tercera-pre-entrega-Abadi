from django.shortcuts import render, redirect
from app.forms import FormularioUsuario, FormularioPosteo, FormularioTest, FormularioBuscarUsuario
from app.models import Usuario, Posteo, Test_Eneagrama

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
        formulario = FormularioPosteo(request.POST, request.FILES)

        if formulario.is_valid():
            info = formulario.cleaned_data
            Posteo(titulo=info["titulo"], imagen=info["imagen"], descripcion=info["descripcion"], usuario=info["usuario"]).save()
            return render(request, 'exito2.html', {"info":info})
    else:
        formulario = FormularioPosteo()

    return render(request, 'hacer_posteo.html', {'formulario': formulario})


def hacer_test(request):
    if request.method == "POST":
        formulario = FormularioTest(request.POST)

        if formulario.is_valid():
            info = formulario.cleaned_data
            Test_Eneagrama(usuario=info["usuario"], eneatipo=info["eneatipo"], energia2=info["energia2"], energia3=info["energia3"]).save()
            return render(request, 'exito3.html', {'formulario': formulario})
    else:
        formulario = FormularioTest()

    return render(request, 'hacer_test.html', {'formulario': formulario})


def buscar_usuario(request):
    formulario = FormularioBuscarUsuario()
    usuarios = None

    if request.method == 'GET' and 'query' in request.GET:
        formulario = FormularioBuscarUsuario(request.GET)
        
        if formulario.is_valid():
            query = formulario.cleaned_data['query']

            usuarios = Usuario.objects.filter(nombre_usuario__iexact=query)

    return render(request, 'buscar_usuario.html', {'formulario': formulario, 'usuarios': usuarios})