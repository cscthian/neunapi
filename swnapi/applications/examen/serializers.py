from rest_framework import serializers, pagination
#
from applications.variables import FULL_DOMAIN
#
from .models import QuestionCategory, Question, Answers


class QuestionCategorySerializer(serializers.ModelSerializer):
    
    class Meta:
        model = QuestionCategory
        fields = ('__all__')


class AnswersSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Answers
        fields = ('__all__')


class QuestionSerializer(serializers.ModelSerializer):
    respuestas = serializers.SerializerMethodField()

    class Meta:
        model = Question
        fields = (
          'category',
          'question',
          'order',
          'points',
          'respuestas',
        )
    
    def get_respuestas(self, obj):
        query = Answers.objects.filter(
           question__id=obj.id
        )
        return AnswersSerializer(query, many=True).data
