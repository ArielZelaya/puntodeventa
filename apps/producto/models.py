from django.db import models

# Create your models here.
class Categoria(models.Model):
	nombre=models.CharField(max_length=50)
	class  Meta:
		verbose_name='categoria'
		verbose_name_plural:'categorias'
	def __str__(self):
		return '%s' %(self.nombre)
class Tipo(models.Model):
	nombre=models.CharField(max_length=50)
	categoria=models.ForeignKey(Categoria,on_delete=models.CASCADE)
	class  Meta:
		verbose_name='tipo'
		verbose_name_plural:'tipos'
	def __str__(self):
		return '%s' %(self.nombre)
		

class Producto(models.Model):
	tipo=models.ForeignKey(Tipo,on_delete=models.CASCADE)
	nombre=models.CharField(max_length=30)
	marca=models.CharField(max_length=30)
	precio=models.DecimalField(max_digits=1000,decimal_places=2)
	codigo=models.CharField(max_length=50)
	descripcion=models.CharField(max_length=150)
	class  Meta:
		verbose_name='producto'
		verbose_name_plural:'productos'
	def __str__(self):
		return '%s' %(self.nombre)



