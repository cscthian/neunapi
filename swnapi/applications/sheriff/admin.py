from django.contrib import admin
from .models import (
    HomeSheriff,
    Agente,
    Mapa,
    Clip,
)

# registro de modelo Producto con su decorador
class HomeSheriffAdmin(admin.ModelAdmin):
    ordering = ['id']
    list_display = (
        'name',
        'username',       
        'link_main',
        'id',
        
    )
    search_fields = ('name', )


# registro de modelo Producto con su decorador
class AgenteAdmin(admin.ModelAdmin):
    ordering = ['id']
    list_display = (
        'name',
        'visits',       
        'order',
        'num_videos',
        'color',
        'public',
        'id',
        
    )
    search_fields = ('name', )


# registro de modelo Producto con su decorador
class MapaAdmin(admin.ModelAdmin):
    ordering = ['id']
    list_display = (
        'name',
        'visits',       
        'order',
        'color',
        'id',
        
    )
    search_fields = ('name', )

class ClipAdmin(admin.ModelAdmin):
    ordering = ['-likes','agente']
    list_display = (
        'name',
        'mapa',
        'agente',
        'tiempo',       
        'video_id',
        'video',
        'id',
    )
    search_fields = ('name', 'agente__name')
    list_filter = ('mapa',)

admin.site.register(HomeSheriff, HomeSheriffAdmin)
admin.site.register(Agente, AgenteAdmin)
admin.site.register(Mapa, MapaAdmin)
admin.site.register(Clip, ClipAdmin)