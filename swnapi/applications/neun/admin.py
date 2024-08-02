from django.contrib import admin
#
from .models import Products


@admin.register(Products)
class ProductsAdmin(admin.ModelAdmin):
    list_display = (
      'title',
      'resume',
      'visits',
      'order',
      'id',
    )
    search_fields = ('title',)
    ordering = ['-order', 'id']
