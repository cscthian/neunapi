from django.contrib import admin
from .models import (
    Product,
    Colors,
    Category,
)

#
class CategoryAdmin(admin.ModelAdmin):
    ordering = ['name']
    list_display = (
        'name',
        'name_unique',
    )
    search_fields = ('name', )


class ColorsAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'value',
    )
    search_fields = ('name', )


# registro de modelo Producto con su decorador
class ProductAdmin(admin.ModelAdmin):
    ordering = ['visits']
    list_display = (
        'name',
        'model',        
        'publicado',
        'visits',
        
    )
    search_fields = ('name', )
    filter_horizontal = (
        'category',
        'colors',
    )
    #   

admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Colors, ColorsAdmin)
