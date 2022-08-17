from django.shortcuts import render
#
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.generics import (
    ListAPIView,
    RetrieveAPIView
)
# serializer
from .serializers import (
    QuestionSerializer
)
#
from applications.tienda.serializers import PaginationSerializer
#
from .models import Question


# Create your views here.
class QuestionListView(ListAPIView):
    pagination_class = PaginationSerializer
    permission_classes = (AllowAny,)
    serializer_class = QuestionSerializer

    def get_queryset(self):

        queryset = Question.objects.filter(
          category__name_unique = self.request.query_params.get('category', '')
        ).order_by('order')

        return queryset