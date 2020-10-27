from django.contrib import admin

# Register your models here.
from .models import Curso


# registro de modelo Producto con su decorador
@admin.register(Curso)
class CursoAdmin(admin.ModelAdmin):
    ordering = ['name']
    list_display = (
        'name',       
        'price',
        'image',
        'id',
    )
    search_fields = ('name', ) 