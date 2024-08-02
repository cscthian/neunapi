from django.shortcuts import render
from django.views.generic import CreateView
from django import forms
# Create your views here.
from rest_framework.authentication import TokenAuthentication, SessionAuthentication
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.permissions import IsAuthenticated

# local
from .serializers import (
    PaginationSerializer,
    HomePortfolioSerializer,
    SkillsSerializer,
    ExperienceSerializer,
    BlogSerializer
)
from .models import (
    HomePortfolio,
    Skills,
    Experience,
    Blog
)

class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ('__all__')

class CreateViewBlog(CreateView):
    model = Blog
    form_class = BlogForm
    template_name = 'home/blog_add.html'
    success_url = '/'


class GetHomePortfolio(RetrieveAPIView):
    lookup_field = 'id'
    serializer_class = HomePortfolioSerializer
    queryset = HomePortfolio.objects.all()
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication, SessionAuthentication]


class ListSkills(ListAPIView):
    serializer_class = SkillsSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication, SessionAuthentication]
    
    def get_queryset(self):
        queryset = Skills.objects.filter(
            portfolio__id = self.request.query_params.get('portfolio', -1),
        ).order_by('order', 'id')
        return queryset


class ListBlog(ListAPIView):
    pagination_class = PaginationSerializer
    serializer_class = BlogSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication, SessionAuthentication]
    
    def get_queryset(self):
        queryset = Blog.objects.filter(
            publicado=True,
            portfolio__id=self.request.query_params.get('portfolio', -1),
            type_blog=self.request.query_params.get('type', 'E'),
        ).order_by('order','-date')
        return queryset


class RetriveBlogSlug(RetrieveAPIView):
    lookup_field = 'slug'
    serializer_class = BlogSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication, SessionAuthentication]

    def get_queryset(self):
        queryset = Blog.objects.filter(
            publicado=True
        ).order_by('-date')
        return queryset


class ListExperiences(ListAPIView):
    serializer_class = ExperienceSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication, SessionAuthentication]
    
    def get_queryset(self):
        queryset = Experience.objects.filter(
            portfolio__id=self.request.query_params.get('portfolio', -1),
        ).order_by('-order')
        return queryset