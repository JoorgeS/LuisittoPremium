from django.db import models

# Create your models here.

class Usuario(models.Model):
    nombre=models.CharField(max_length=30, verbose_name='Nombre')
    correo=models.EmailField(primary_key=True, verbose_name='Correo')
    telefono=models.CharField(max_length=14, verbose_name='Telefono')
    def __str__(self):
        return self.correo

class Cuentas(models.Model):
    nombreCuenta=models.CharField(primary_key=True,max_length=30, verbose_name='nombre de la cuenta')
    precio=models.IntegerField(verbose_name='Precio')
    duracion=models.CharField(max_length=20, verbose_name='Duracion Cuenta')
    def __str__(self):
        return self.nombreCuenta

class Oferta(models.Model):
    tipoCuenta=models.CharField(primary_key=True,max_length=30)
    descuento=models.IntegerField()
    fechaOferta=models.DateField()
    def __str__(self):
        return self.IDcuenta