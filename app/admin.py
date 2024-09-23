from django.contrib import admin
from .models import Usuario, Test_Eneagrama, Posteo  # Importa los modelos

# Registra los modelos en el administrador
admin.site.register(Usuario)
admin.site.register(Test_Eneagrama)
admin.site.register(Posteo)