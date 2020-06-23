from django.db import models
from django.urls import reverse
from django.utils.html import mark_safe

# Create your models here.
DEPARTAMENTO_CHOICES = (
	('1' ,'Distribucion'),
	('2' ,'Comercial'),
	('3' ,'Generacion'),
	('4' ,'Transmision'),
	('5' ,'Uree'),
	('6' ,'P y P'),
	('7' ,'Bienes y Servicios'),
	('8' ,'ASHO'),
	('9' ,'Talento Humano'),
	('10' ,'Procura'),
	('11' ,'Auditoria Interna'),
	('12' ,'Desarrolo Social'),
	('13' ,'Finanzas Lara'),
	('14' ,'Planificacion Lara'),
	('15' ,'Desarrollo (Ingenieria)'),
	('16' ,'Despacho'),
	('17' ,'ATIT'),
	('18' ,'Fiscalizacion'),
	('19' ,'Proyectos mayores'),
	('20' ,'Comunicaciones Corporativas'),
	('21' ,'Mesas de Energias'),
	('22' ,'COD'),
	('23' ,'Consultoria Juridica'),
	('24' ,'Tesoreria'), )

class Empleado(models.Model):

	CI = models.CharField(max_length=8, unique=True, help_text="Solo colocar numeros")
	Apellidos = models.CharField(max_length=64, help_text="Solo colocar caracteres")
	Nombres = models.CharField(max_length=64, help_text="Solo colocar caracteres")
	Departamento = models.CharField(max_length=255, choices= DEPARTAMENTO_CHOICES, help_text="Coloque el Departamento en donde trabaja")
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
		return mark_safe('<a class="grp-button" href="%s" target="blank">Ver Carnet</a>' % reverse('Empleados:pdf', args=[self.CI]))
	carnet.short_description = ('Carnet')