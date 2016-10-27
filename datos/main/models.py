from django.db import models
from django.contrib.auth.models import User

class Perfil(models.Model):
	SEXO=(('hombre','HOMBRE'),('mujer','MUJER'))
	OCUP=(
		('estudiante','Estudiante'),
		('academico','Academico'),
		('empresario','Empresario'),
		('godinez','Empleado')
		)

	edad=models.IntegerField()
	tel=models.CharField(max_length=13)
	genero=models.CharField(max_length=6,choices=SEXO)
	alias=models.CharField(max_length=10)
	domicilio=models.TextField()
	ocupacion=models.CharField(max_length=140,choices=OCUP)
	usuario=models.OneToOneField(User)


class Producto(models.Model):
	nombre=models.CharField(max_length=140)
	desc=models.TextField()
	precio=models.CharField(max_length=50)
	usuario=models.ForeignKey(User,related_name='productos')
	
	def __str__(self):
		return self.nombre