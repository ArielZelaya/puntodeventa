from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Cliente(User):
    dui = models.IntegerField()
    telefono = models.IntegerField()
    direccion = models.CharField(max_length=500)
    tipo = models.CharField(max_length=1)
    class Meta:
        verbose_name='Cliente'
        verbose_name_plural='Clientes'
    def __str__(self):
        return '%s' %(self.first_name)

class Empleado(User):
	dui = models.IntegerField()
	nit = models.IntegerField()
	isss = models.IntegerField()
	nup = models.IntegerField()
	domicilio = models.CharField(max_length=500)
	telefono = telefono = models.IntegerField()
	class Meta:
		verbose_name='Empleado'
		verbose_name_plural='Empleados'
	def __str__(self):
		return '%s' %(self.first_name)