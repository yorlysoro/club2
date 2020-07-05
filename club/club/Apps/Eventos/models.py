from django.db import models
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
# Create your models here.

class Eventos(models.Model):
    titulo = models.CharField('Titulo del Evento', max_length=512, unique=True)
    publicado = models.BooleanField('Publicado/No Publicado', default=False)
    fecha_creacion = models.DateField('Fecha de Creacion', auto_now=False, auto_now_add=True)
    descripcion = models.TextField('Descripcion', max_length=1024)
    contenido = RichTextUploadingField()
    imagen_referencial = models.ImageField('Imagen Referencial', upload_to='media/eventos', max_length=255)

    class Meta:
        verbose_name = 'Evento'
        verbose_name_plural = 'Eventos'
    
    def __str__(self):
        return self.titulo
    