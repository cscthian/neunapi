from rest_framework import serializers, pagination
#
from applications.variables import FULL_DOMAIN


from .models import Curso



class PaginationSerializer(pagination.PageNumberPagination):
    
    page_size = 9
    max_page_size = 50


class CursoSerializer(serializers.ModelSerializer):

    image = serializers.SerializerMethodField()

    class Meta:
        model = Curso
        fields = ('__all__')
    
    def get_image(self, obj):
        if obj.image:
            return FULL_DOMAIN + obj.image.url
        else:
            return None
