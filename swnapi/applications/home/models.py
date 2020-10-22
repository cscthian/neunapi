from django.db import models

# Create your models here.
from ckeditor.fields import RichTextField

# Django
from django.conf import settings


class Servicios(models.Model):
    """ Servicios api  """

    name = models.CharField(
        'nombre', 
        max_length=120
    )
    content = RichTextField(
        'contenido'
    )
    video = models.URLField(blank=True)
    publicado = models.BooleanField(default=False)
    visits = models.IntegerField(default=0)

    class Meta:
        verbose_name = 'Servicio'
        verbose_name_plural = 'Servicios API'

    def __str__(self):
        return self.name

        
