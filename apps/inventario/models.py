from django.db import models
from apps.producto.models import Producto
# Create your models here.
class Mercancia(models.Model):
	Producto=models.ForeignKey(Producto,on_delete=models.CASCADE)
	cantidad=models.IntegerField(null=True)
	class  Meta:
		verbose_name='Mercancia'
		verbose_name_plural='Mercancias'
	def __str__(self):
		return '%s' %(self.Producto.nombre)
