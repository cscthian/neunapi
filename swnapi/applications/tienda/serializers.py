from rest_framework import serializers, pagination
#
from applications.variables import FULL_DOMAIN
#
from .models import Product, Category, Colors

class PaginationSerializer(pagination.PageNumberPagination):
    """ serializador para paginacion en listas """
    page_size = 12
    max_page_size = 50


class ColorsSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Colors
        fields = ('__all__')


class CategorySerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Category
        fields = ('__all__')


class ProductSerializer(serializers.ModelSerializer):
    
    colors = ColorsSerializer(many=True)
    category = CategorySerializer(many=True)
    main_image = serializers.SerializerMethodField()
    second_image = serializers.SerializerMethodField()
    third_image = serializers.SerializerMethodField()
    
    class Meta:
        model = Product
        fields = ('__all__')
    
    def get_main_image(self, obj):
        if obj.main_image:
            return FULL_DOMAIN + obj.main_image.url
        else:
            return None
    
    def get_second_image(self, obj):
        if obj.second_image:
            return FULL_DOMAIN + obj.second_image.url
        else:
            return None
    
    def get_third_image(self, obj):
        if obj.third_image:
            return FULL_DOMAIN + obj.third_image.url
        else:
            return None

