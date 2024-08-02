from django.contrib import admin
from .models import Blog, Experience, HomePortfolio, Skills
#
@admin.register(HomePortfolio)
class HomePortfolioAdmin(admin.ModelAdmin):
  list_display = (
    'title',
    'subtitle',
    'visits',
    'id',
  )
  search_fields = ('title',)
  
  
@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
  list_display = (
    'portfolio',
    'type_blog',
    'title',
    'slug',
    'publicado',
    'date',
    'visits',
    'id',
  )
  search_fields = ('title', 'type_blog',)
  ordering = ('portfolio', '-date', 'title')

  
@admin.register(Skills)
class SkillsAdmin(admin.ModelAdmin):
  list_display = (
    'portfolio',
    'title',
    'nivel',
    'order',
    'link',
    'id',
  )
  search_fields = ('title',)
  ordering = ('portfolio', 'order', '-id')


@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
  list_display = (
    'portfolio',
    'title',
    'subtitle',
    'link_blog',
    'description',
    'order',
    'id',
  )
  search_fields = ('title',)
  ordering = ('portfolio', 'order', '-id')