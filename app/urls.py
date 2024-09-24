from django.urls import path
from app.views import *

urlpatterns = [
    path('', bienvenida, name='bienvenida'),
    path('ingresar_usuario.html', ingresar_usuario, name='ingresar_usuario' ),
    path('hacer_posteo.html', hacer_posteo, name='hacer_posteo'),
    path('hacer_test.html', hacer_test, name='hacer_test'),
    path('buscar_usuario.html', buscar_usuario, name='buscar_usuario' )
]