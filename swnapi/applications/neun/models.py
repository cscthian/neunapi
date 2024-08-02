from datetime import timedelta, datetime
from django.template.defaultfilters import slugify
from django.db import models

# Productos de Software Neun
class Products(models.Model):
    """ Productos desarrollador pos grupo neun """

    APPS = 'A'
    WEB = 'W'
    PACKAGE = 'P'
    TIPE_PROD = [
      (APPS, 'Aplicativos'),
      (WEB, 'Web App'),
      (PACKAGE, 'Paquetes dev'),
    ]

    type_blog = models.CharField(
      'Tipo Producto', 
      max_length=1,
      choices=TIPE_PROD
    )
    title = models.CharField(
        'titulo', 
        max_length=120
    )
    resume = models.TextField(
      'Resumen Prod', 
    )
    tag = models.CharField(
        'tag', 
        max_length=30
    )
    image = models.ImageField(
        'Imagen Prod', 
        upload_to='prod-neun',
        blank=True,
        null=True
    )
    publicado = models.BooleanField(default=False)
    video = models.URLField(blank=True)
    link = models.URLField(blank=True)
    date = models.DateField('Fecha Publicacion')
    visits = models.PositiveIntegerField(default=0)
    order = models.PositiveIntegerField(default=0)
    slug = models.SlugField(
        max_length=250,
        blank=True
    )

    class Meta:
        verbose_name = 'Productos Neun'
        verbose_name_plural = 'Productos Neun'

    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        if not self.id:
            # calculamos el total de segundos de la hora actual
            now = datetime.now()
            total_time = timedelta(
                hours=now.hour,
                minutes=now.minute,
                seconds=now.second
            )
            seconds = int(total_time.total_seconds())
            slug_unique = '%s %s' % (self.title, str(seconds))
        else:
            # seconds = self.slug.split('-')[-1]  # recuperamos los segundos
            slug_unique = self.slug

        self.slug = slugify(slug_unique)
        super(Products, self).save(*args, **kwargs)