from datetime import timedelta, datetime
from django.template.defaultfilters import slugify

from django.db import models

# Create your models here.
from django.contrib.postgres.fields import ArrayField
from django_quill.fields import QuillField

# Django
class HomePortfolio(models.Model):
    """ Home de portafolio  """
    title_mov = models.CharField('titulo en movil', max_length=100)
    title = models.CharField(
        'titulo', 
        max_length=120
    )
    subtitle = models.CharField(
        'sub titulo', 
        max_length=120
    )
    description = models.CharField(
      'descripcion', 
      max_length=200
    )
    photo = models.ImageField(
        'Foto', 
        upload_to='photo-portfolio',
        blank=True,
        null=True
    )
    text_footer = models.CharField(
      'Mensaje Footer', 
      max_length=200
    )
    visits = models.IntegerField(default=0)
    contry = models.CharField(
      'pais', 
      max_length=50
    )
    linkeding = models.URLField(blank=True)
    github = models.URLField(blank=True)
    title_seo = models.CharField(
      'Titulo SEO', 
      max_length=200
    )
    description_seo = models.CharField(
      'Descripcion SEO', 
      max_length=200
    )
    kwords = ArrayField(
      models.CharField(max_length=50), 
      blank=True
    )

    class Meta:
        verbose_name = 'Home Portafolio'
        verbose_name_plural = 'Home Pages'

    def __str__(self):
        return self.title

        
class Blog(models.Model):
    """ Blog personal  """

    PROYECTO = 'P'
    IDNI = 'I'
    ENTRADA = 'B'
    TIPE_BLOG = [
      (PROYECTO, 'Proyecto'),
      (IDNI, 'Proyecto INDI'),
      (ENTRADA, 'Blog'),
    ]
    
    portfolio = models.ForeignKey(HomePortfolio, on_delete=models.CASCADE)
    type_blog = models.CharField(
      'Tipo blog', 
      max_length=1,
      choices=TIPE_BLOG
    )
    title = models.CharField(
        'titulo', 
        max_length=120
    )
    resume = models.TextField(
      'Resumen Blog', 
      max_length=170
    )
    image = models.ImageField(
        'Imagen Blog', 
        upload_to='blog-portfolio',
        blank=True,
        null=True
    )
    type_article = models.CharField(
      'Topo Articulo', 
      max_length=30,
      blank=True
    )
    tags = ArrayField(
      models.CharField(max_length=50), 
      blank=True
    )
    publicado = models.BooleanField(default=False)
    video = models.URLField(blank=True)
    date = models.DateField('Fecha Publicacion')
    visits = models.PositiveIntegerField()
    order = models.PositiveIntegerField()
    content = QuillField()
    slug = models.SlugField(
        max_length=250,
        blank=True
    )

    class Meta:
        verbose_name = 'Blog Portfolio'
        verbose_name_plural = 'Blogs'

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
        super(Blog, self).save(*args, **kwargs)



class Skills(models.Model):
    """ Habilidades Portfolio  """

    portfolio = models.ForeignKey(HomePortfolio, on_delete=models.CASCADE)
    title = models.CharField(
        'titulo', 
        max_length=120
    )
    logo = models.ImageField(
        'logo', 
        upload_to='skills-portfolio',
        blank=True,
        null=True
    )
    nivel = models.CharField(
      'Nivel', 
      max_length=25
    )
    link = models.URLField(blank=True)
    link_certificate = models.URLField(blank=True)
    order = models.PositiveIntegerField()

    class Meta:
        verbose_name = 'Skills portfolio'
        verbose_name_plural = 'Skills portfolio'

    def __str__(self):
        return self.title


class Experience(models.Model):
    """ Experiencia laboral portfolio  """

    portfolio = models.ForeignKey(HomePortfolio, on_delete=models.CASCADE)
    title = models.CharField(
        'titulo', 
        max_length=120
    )
    subtitle = models.CharField(
        'subtitulo', 
        max_length=150
    )
    description = models.CharField(
      'Descripcion', 
      max_length=100
    )
    skills = ArrayField(
      models.CharField(max_length=50), 
      blank=True
    )
    link_blog = models.URLField(blank=True)
    order = models.PositiveIntegerField()

    class Meta:
        verbose_name = 'Experiencia Laboral'
        verbose_name_plural = 'Experiencia Laboral'

    def __str__(self):
        return self.title