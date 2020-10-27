from django.db import models

# Create your models here.
from ckeditor.fields import RichTextField


class Curso(models.Model):
    """ Cursos  """

    name = models.CharField(
        'nombre', 
        max_length=150
    )
    price = models.DecimalField(
        'Precio unidad', 
        max_digits=10, 
        decimal_places=3
    )
    decription = RichTextField(
        'Descripcion del Producto'
    )
    image = models.ImageField(
        'Imagen Curso', 
        upload_to='Cursos',
        blank=True,
        null=True
    )

    class Meta:
        verbose_name = 'Curso'
        verbose_name_plural = 'Cursos'

    def __str__(self):
        return self.name

        
