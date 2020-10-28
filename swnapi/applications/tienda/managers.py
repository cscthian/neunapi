from django.db import models

from django.utils import timezone
# Create your models here.
#
from django.db.models import Q
from django.contrib.postgres.search import TrigramSimilarity


class ProductMananger(models.Manager):
    """ procedimientos para modelo """
    
    def por_categoria(self, **filters):
        #
        consulta = self.filter(
            publicado=True,
            name__icontains=filters['name']
        ).order_by('-visits')

        if (len(filters['category']) > 4):
            consulta = consulta.filter(
                category__name_unique=filters['category'],
            )
        
        colores = filters['colors'].split(',')
        if len(filters['colors']) > 0:
            consulta = consulta.filter(
                publicado=True,
                colors__id__in=colores,
            )

        if filters['order'] == 'name':
            return consulta.order_by('name')
        elif filters['order'] == 'gprice':
            return consulta.order_by('-price')
        elif filters['order'] == 'sprice':
            return consulta.order_by('price')
        else:
            return consulta.order_by('-visits')


class CategoryMananger(models.Manager):

    def search_categorys(self):
        # funcion que lista 
        resultado = self.filter(
            name__icontains=name
        )
        #
        return resultado