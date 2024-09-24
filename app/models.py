from django.db import models

#usuarios

#tipos de eneagrama

#Posteos

class Usuario(models.Model):
    nombre_usuario = models.CharField(max_length=80)
    nombre_completo = models.CharField(max_length=80)
    email = models.EmailField()
    contrasena = models.CharField(max_length=80)
    genero = models.CharField(max_length=80)
    edad = models.IntegerField()

    def __str__(self) -> str:
        return self.nombre_usuario
    
    
class Test_Eneagrama(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.SET_NULL, null=True, blank=True)
    eneatipo = models.IntegerField()
    energia2 = models.IntegerField()
    energia3 = models.IntegerField()

    def __str__(self):
        return self.usuario.nombre_usuario if self.usuario else "Usuario no asignado"
    

class Posteo(models.Model):
    titulo = models.CharField(max_length=80, default="Sin titulo")
    imagen = models.ImageField()
    descripcion = models.TextField()
    usuario = models.ForeignKey(Usuario, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self) -> str:
        return self.titulo
    


