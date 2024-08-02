from rest_framework import serializers
#
from .models import Products

from applications.variables import FULL_DOMAIN

class ProductosSerializers(serializers.ModelSerializer):
    
    image = serializers.SerializerMethodField()

    class Meta:
        model = Products
        fields = (
            '__all__'
        )
    
    def get_image(self, obj):
        if obj.image:
            return FULL_DOMAIN + obj.image.url
        else:
            return None