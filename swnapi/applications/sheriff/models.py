from django.db import models

# Create your models here.
from ckeditor.fields import RichTextField


class HomeSheriff(models.Model):

    name = models.CharField(
        'nombre', 
        max_length=50
    )
    username = models.CharField(
        'username', 
        max_length=30
    )
    logo_image = models.ImageField(
        'Imagen logo', 
        upload_to='sheriffLogo',
        blank=True,
        null=True
    )
    link_main = models.URLField(blank=True)
    link_uno = models.URLField(blank=True)
    link_dos = models.URLField(blank=True)

    class Meta:
        verbose_name = 'Home'
        verbose_name_plural = 'Home Sheriff'

    def __str__(self):
        return self.name

        
class Mapa(models.Model):

    name = models.CharField(
        'nombre', 
        max_length=50
    )
    visits = models.PositiveIntegerField(default=0)
    order = models.PositiveIntegerField(default=0)
    image = models.ImageField(
        'Imagen', 
        upload_to='sheriffMapa',
        blank=True,
        null=True
    )
    color = models.CharField('color', max_length=10, blank=True)
    description = RichTextField(
        'Descripcion Mapa',
        blank=True,
    )

    class Meta:
        verbose_name = 'Mapa'
        verbose_name_plural = 'Mapas'

    def __str__(self):
        return self.name


class Agente(models.Model):

    name = models.CharField(
        'nombre', 
        max_length=50
    )
    visits = models.PositiveIntegerField(default=0)
    order = models.PositiveIntegerField(default=0)
    num_videos = models.PositiveIntegerField(default=0)
    image = models.ImageField(
        'Imagen', 
        upload_to='sheriffMapa',
        blank=True,
        null=True
    )
    color = models.CharField('color', max_length=10, blank=True)
    contenido = RichTextField(
        'Descripcion Mapa'
    )
    public = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'Agente'
        verbose_name_plural = 'Agentes'

    def __str__(self):
        return self.name


class Clip(models.Model):

    agente = models.ForeignKey(
        Agente, 
        on_delete=models.CASCADE, 
        verbose_name='agente_clip',
        related_query_name='agente_clip',)
    mapa = models.ForeignKey(
        Mapa, 
        on_delete=models.CASCADE, 
        verbose_name='mapa_clip', 
        related_query_name='mapa_clip',)
    name = models.CharField(
        'nombre', 
        max_length=50
    )
    image = models.ImageField(
        'Imagen logo', 
        upload_to='sheriffLogo',
        blank=True,
        null=True
    )
    image_uno = models.ImageField(
        'Imagen uno', 
        upload_to='sheriffimg',
        blank=True,
        null=True
    )
    image_dos = models.ImageField(
        'Imagen dos', 
        upload_to='sheriffimg',
        blank=True,
        null=True
    )
    video = models.URLField(blank=True)
    video_id = models.CharField('video id', max_length=30)
    tiempo = models.CharField('tiempo', max_length=5)
    likes = models.PositiveIntegerField(default=0)

    class Meta:
        verbose_name = 'Clip'
        verbose_name_plural = 'Clips'

    def __str__(self):
        return self.name