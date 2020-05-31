from django.db import models
from django.urls import reverse
from django.utils.html import mark_safe

# Create your models here.

class Empleado(models.Model):

	CI = models.CharField(max_length=8, unique=True, help_text="Solo colocar numeros")
	Apellidos = models.CharField(max_length=64, help_text="Solo colocar caracteres")
	Nombres = models.CharField(max_length=64, help_text="Solo colocar caracteres")
	Departamento = models.CharField(max_length=255, help_text="Coloque el Departamento en donde trabaja")
	Carga_Familiar = models.IntegerField()
	FechaNacimiento = models.DateField(help_text="Coloque su fecha de nacimiento en formato dia/mes/año")
	sexo = [
		('M' , 'Masculino'),
		('F' , 'Femenino'),
	]
	Sexo = models.CharField(max_length=2, choices=sexo, default='M')
	Correo = models.EmailField(blank=True, null=True, help_text="Coloque una direccion de correo valida")
	Foto = models.ImageField(upload_to='fotos/')
	Carnet = models.FileField(upload_to='carnet/', null=True, blank=True)
	Activo = models.BooleanField(default=False)
	Numero_Personal = models.CharField(max_length=256)

	def __str__(self):
		return '{0}, {1}, {2}'.format(self.CI, self.Apellidos, self.Nombres)

	def carnet(self):
		return mark_safe('<a class="grp-button" href="%s" target="blank">Ver Carnet</a>' % reverse('Empleados:carnet', args=[self.CI]))
	carnet.short_description = ('Carnet')