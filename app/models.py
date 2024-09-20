from django.db import models

#usuarios

#tipos de eneagrama

#Posteos

class Usuario(models.Model):
    nombre = models.CharField(max_length=80)
    apellido = models.CharField(max_length=80)
    email = models.EmailField()
    contrasena = models.CharField(max_length=80)
    genero = models.CharField(max_length=80)
    edad = models.IntegerField()

    def __str__(self) -> str:
        return self.nombre
    
class Test_Eneagrama(models.Model):
    eneatipo = models.IntegerField()
    energia2 = models.IntegerField()
    energia3 = models.IntegerField()

class Posteo(models.Model):
    imagen = models.ImageField()
    descripcion = models.TextField()
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)