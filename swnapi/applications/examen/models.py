from django.db import models

# Create your models here.
class QuestionCategory(models.Model):
    """Modelo que representa categorias de un producto """

    name = models.CharField('Categoria', max_length=50)
    name_unique = models.CharField('Nombre Unico', max_length=25, unique=True)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        verbose_name = 'Categoria Pregunta'
        verbose_name_plural = 'Categoria preguntas'

    def __str__(self):
        return str(self.id) + ' ' + str(self.name)


class Question(models.Model):
    """Modelo que representa categorias de un producto """

    category = models.ForeignKey(QuestionCategory, on_delete=models.CASCADE)
    question = models.CharField('Pregunta', max_length=200)
    order = models.PositiveIntegerField(default=0)
    points = models.PositiveIntegerField(default=0)
    #

    class Meta:
        verbose_name = 'Pregunta'
        verbose_name_plural = 'Preguntas'

    def __str__(self):
        return str(self.category.name) + ' - ' + str(self.question)


class Answers(models.Model):
    """Modelo que respuestas verdaderas y falsas"""

    question = models.ForeignKey(
        Question, 
        on_delete=models.CASCADE,
        related_query_name='answers_questions'
    )
    answer = models.CharField('Alternativa', max_length=100)
    tag = models.CharField('Etiqueta', max_length=2, blank=True)
    order = models.PositiveIntegerField(default=0)
    is_true = models.BooleanField(default=False)
    #

    class Meta:
        verbose_name = 'Respuesta - Alternativa'
        verbose_name_plural = 'Respuestas - Alternativas'

    def __str__(self):
        return str(self.question.question) + ' - ' + str(self.answer)