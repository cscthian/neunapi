from django.contrib import admin
from .models import (
    Servicios,
)

# registro de modelo Producto con su decorador
class ServiciosAdmin(admin.ModelAdmin):
    ordering = ['visits']
    list_display = (
        'name',
        'id',       
        'publicado',
        'visits',
        
    )
    search_fields = ('name', )
    #   

admin.site.register(Servicios, ServiciosAdmin)
