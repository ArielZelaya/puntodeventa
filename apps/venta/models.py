from django.db import models
from apps.usuario.models import Cliente
from apps.producto.models import Producto
from .models import *

# Create your models here.

class Venta(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    fecha = models.DateTimeField()
    total = models.FloatField()
    class Meta:
        verbose_name = 'Venta'
        verbose_name_plural = 'Ventas'
    def __str__(self):
        return '%s' % (self.cliente.first_name)


class Linea(models.Model):
    venta = models.ForeignKey(Venta, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.IntegerField()
    subtotal = models.FloatField()
    class Meta:
        verbose_name = 'Linea de venta'
        verbose_name_plural = 'Lineas de venta'
    def __str__(self):
        return '%s' % (self.venta.cliente.username)