from django.db import models
from ckeditor.fields import RichTextField
# Create your models here.

class Eventos(models.Model):
    titulo = models.CharField('Titulo del Evento', max_length=255, unique=True)
    publicado = models.BooleanField('Publicado/No Publicado', default=False)
    fecha_creacion = models.DateField('Fecha de Creacion', auto_now=False, auto_now_add=True)
    descripcion = models.TextField('Descripcion')
    contenido = RichTextField()
    imagen_referencial = models.ImageField('Imagen Referencial', upload_to='media/eventos', max_length=255)

    class Meta:
        verbose_name = 'Evento'
        verbose_name_plural = 'Eventos'