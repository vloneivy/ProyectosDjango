from django.db import models

# Create your models here.

# Create Modelo para Categoria

class Categoria(models.Model):
    idCategoria = models.IntegerField(primary_key=True, verbose_name="Id de categoría")
    nombreCategoria = models.CharField(max_length=80, blank=False, null=False, verbose_name="Nombre de la categoría")

    def __str__(self):
        return self.nombreCategoria

# Create Modelo para vehículo

class Vehiculo(models.Model):
    ID = models.CharField(max_length=6, primary_key=True, verbose_name="ID")
    marca = models.CharField(max_length=80, blank=False, null=False, verbose_name="Marca vehículo")
    modelo = models.CharField(max_length=80, null=True, blank=True, verbose_name="Modelo")
    imagen = models.ImageField(upload_to="images/", default="sinfoto.jpg", null=False, blank=False, verbose_name="Imagen")
    categoria = models.ForeignKey(Categoria, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.ID
