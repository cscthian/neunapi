from django.contrib import admin

from .models import (
  QuestionCategory,
  Question,
  Answers
)

# Register your models here.
class QuestionCategoryAdmin(admin.ModelAdmin):
    ordering = ['order']
    list_display = (
        'name',
        'name_unique',
        'order',
    )
    search_fields = ('name', )


class QuestionAdmin(admin.ModelAdmin):
    ordering = ['order']
    list_display = (
        'category',
        'question',
        'order',
        'points',
    )
    search_fields = ('question', )


class AnswersAdmin(admin.ModelAdmin):
    ordering = ['order']
    list_display = (
        'question',
        'answer',
        'order',
        'is_true',
    )
    search_fields = ('answer', )

admin.site.register(QuestionCategory, QuestionCategoryAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Answers, AnswersAdmin)