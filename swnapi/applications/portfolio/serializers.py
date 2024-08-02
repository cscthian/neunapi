from rest_framework import serializers, pagination
#
from applications.variables import FULL_DOMAIN
#
from .models import (
  HomePortfolio, 
  Blog, 
  Skills, 
  Experience
)

class PaginationSerializer(pagination.PageNumberPagination):
    """ serializador para paginacion en listas """
    page_size = 12
    max_page_size = 50


class HomePortfolioSerializer(serializers.ModelSerializer):
    
    photo = serializers.SerializerMethodField()
    
    class Meta:
        model = HomePortfolio
        fields = (
          '__all__'
        )
    
    def get_photo(self, obj):
        if obj.photo:
            return FULL_DOMAIN + obj.photo.url
        else:
            return None


class BlogSerializer(serializers.ModelSerializer):
    
    image = serializers.SerializerMethodField()
    content = serializers.SerializerMethodField()
    
    class Meta:
        model = Blog
        fields = (
          '__all__'
        )
    
    def get_content(self, obj):
        return obj.content.html

    def get_image(self, obj):
        if obj.image:
            return FULL_DOMAIN + obj.image.url
        else:
            return None


class SkillsSerializer(serializers.ModelSerializer):
    
    logo = serializers.SerializerMethodField()
    
    class Meta:
        model = Skills
        fields = (
          '__all__'
        )
    
    def get_logo(self, obj):
        if obj.logo:
            return FULL_DOMAIN + obj.logo.url
        else:
            return None


class ExperienceSerializer(serializers.ModelSerializer):
  
    class Meta:
        model = Experience
        fields = (
          '__all__'
        )