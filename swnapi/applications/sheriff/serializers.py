from rest_framework import serializers, pagination
#
from applications.variables import FULL_DOMAIN
#
from .models import Mapa, HomeSheriff, Agente, Clip

class PaginationSerializer(pagination.PageNumberPagination):
    """ serializador para paginacion en listas """
    page_size = 16
    max_page_size = 50


class HomeSheriffSerializer(serializers.ModelSerializer):
    get_logo_image = serializers.SerializerMethodField()
    
    class Meta:
        model = HomeSheriff
        fields = ('__all__')
    
    def get_logo_image(self, obj):
        if obj.logo_image:
            return FULL_DOMAIN + obj.logo_image.url
        else:
            return FULL_DOMAIN + '/static/img/noimage.png'


class MapaSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField()
    
    class Meta:
        model = Mapa
        fields = ('__all__')
    
    def get_image(self, obj):
        if obj.image:
            return FULL_DOMAIN + obj.image.url
        else:
            return FULL_DOMAIN + '/static/img/noimage.png'


class AgenteSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField()
    
    class Meta:
        model = Agente
        fields = ('__all__')
    
    def get_image(self, obj):
        if obj.image:
            return FULL_DOMAIN + obj.image.url
        else:
            return FULL_DOMAIN + '/static/img/noimage.png'


class AgenteSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField()
    
    class Meta:
        model = Agente
        fields = ('__all__')
    
    def get_image(self, obj):
        if obj.image:
            return FULL_DOMAIN + obj.image.url
        else:
            return FULL_DOMAIN + '/static/img/noimage.png'
    
    def get_image_uno(self, obj):
        if obj.image_uno:
            return FULL_DOMAIN + obj.image_uno.url
        else:
            return FULL_DOMAIN + '/static/img/noimage.png'
    
    def get_image_dos(self, obj):
        if obj.image_dos:
            return FULL_DOMAIN + obj.image_dos.url
        else:
            return FULL_DOMAIN + '/static/img/noimage.png'


class ClipSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField()
    agente_name = serializers.SerializerMethodField()
    mapa_name = serializers.SerializerMethodField()
    
    class Meta:
        model = Clip
        fields = (
            'id',
            'agente',
            'mapa',
            'name',
            'image',
            'video',
            'video_id',
            'tiempo',
            'likes',
            'agente_name',
            'mapa_name',
        )
    
    def get_image(self, obj):
        if obj.image:
            return FULL_DOMAIN + obj.image.url
        else:
            return FULL_DOMAIN + '/static/img/noimage.png'
    
    def get_agente_name(self, obj):
        return obj.agente.name
    
    def get_mapa_name(self, obj):
        return obj.mapa.name