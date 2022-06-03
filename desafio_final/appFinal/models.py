from django.db import models

# Create your models here.


class Productos(models.Model):
    nombre = models.CharField(max_length=40)
    precio = models.IntegerField()
    
class Usuarios(models.Model):
    nombre = models.CharField(max_length=40)
    dni = models.IntegerField()


class Peliculas(models.Model):
    nombre = models.CharField(max_length=50)
    precio = models.IntegerField()