from django.db import models

# Create your models here.
from ckeditor.fields import RichTextField

# Django
from django.conf import settings

#
from .managers import (
    CategoryMananger, 
    ProductMananger
)


class Category(models.Model):
    """Modelo que representa categorias de un producto """

    name = models.CharField('Nombre de la Categoria', max_length=50)
    name_unique = models.CharField('Nombre Unico', max_length=25, unique=True)
    objects = CategoryMananger()

    class Meta:
        verbose_name = 'Categoria Producto'
        verbose_name_plural = 'Categoria productos'

    def __str__(self):
        return str(self.id) + ' ' + str(self.name)


#  ------------- Modelo Color -----------------
class Colors(models.Model):
    """ Color """

    name = models.CharField(
        'nombre', 
        max_length=30
    )
    value = models.CharField(
        'valor HEX', 
        max_length=7
    )

    class Meta:
        verbose_name = 'Color'
        verbose_name_plural = 'Colores'

    def __str__(self):
        return self.name


class Product(models.Model):
    """ Producto  """

    name = models.CharField(
        'nombre', 
        max_length=120
    )
    category = models.ManyToManyField(
        Category,
        verbose_name="categoria"
    )
    colors = models.ManyToManyField(
        Colors,
        verbose_name="colores",
    )
    price = models.DecimalField(
        'Precio unidad', 
        max_digits=10, 
        decimal_places=3
    )
    decription = RichTextField(
        'Descripcion del Producto'
    )
    main_image = models.ImageField(
        'Imagen Principal', 
        upload_to='producto',
        blank=True,
        null=True
    )
    second_image = models.ImageField(
        'Imagen 2',
        upload_to='producto',
        blank=True,
        null=True
    )
    third_image = models.ImageField(
        'Imagen 3',
        upload_to='producto',
        blank=True,
        null=True
    )
    publicado = models.BooleanField(default=False)
    visits = models.IntegerField(default=0)

    #
    objects = ProductMananger()

    class Meta:
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'

    def __str__(self):
        return self.name

        
