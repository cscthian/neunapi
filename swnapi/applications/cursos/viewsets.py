from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes, action
from rest_framework.permissions import IsAuthenticated, AllowAny
#
from .models import Curso
#
from .serializers import (
    CursoSerializer,
    PaginationSerializer
)

class CursoViewSet(viewsets.ModelViewSet):
    """  """
    serializer_class = CursoSerializer
    queryset = Curso.objects.all()
    pagination_class = PaginationSerializer

    def get_permissions(self):
        """
        permisos de usuario
        """
        if (self.action == 'list') or (self.action == 'retrieve'):
            permission_classes = [AllowAny]
        else:
            permission_classes = [IsAuthenticated]
        return [permission() for permission in permission_classes]