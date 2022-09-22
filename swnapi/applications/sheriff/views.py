#
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.generics import (
    ListAPIView,
    RetrieveAPIView
)
# serializer
from .serializers import (
    PaginationSerializer,
    HomeSheriffSerializer,
    MapaSerializer,
    AgenteSerializer,
    ClipSerializer,
)
#
#
from .models import HomeSheriff, Mapa, Agente, Clip


# Create your views here.
class GetHomeSheriff(RetrieveAPIView):
    serializer_class = HomeSheriffSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def retrieve(self, request, *args, **kwargs):
        home = HomeSheriff.objects.all()[0]
        serializer = self.get_serializer(home)
        return Response(serializer.data)


# Create your views here.
class MapasListView(ListAPIView):
    pagination_class = PaginationSerializer
    permission_classes = (AllowAny,)
    serializer_class = MapaSerializer
    
    def get_queryset(self):
        queryset = Mapa.objects.filter(
          name__icontains = self.request.query_params.get('name', '')
        ).order_by('order')

        return queryset


class AgentesListView(ListAPIView):
    pagination_class = PaginationSerializer
    permission_classes = (AllowAny,)
    serializer_class = AgenteSerializer
    
    def get_queryset(self):
        resultado = Agente.objects.filter(
          name__icontains = self.request.query_params.get('name', ''),
          public=True,
        ).order_by('-visits','order')

        return resultado

class AgentesByMapaListView(ListAPIView):
    pagination_class = PaginationSerializer
    permission_classes = (AllowAny,)
    serializer_class = AgenteSerializer
    
    def get_queryset(self):
        resultado = Agente.objects.filter(
          agente_clip__mapa__id = self.request.query_params.get('mapa', ''),
          public=True,
        ).distinct().order_by('-visits','order')
        print(resultado)
        return resultado


class ClipsListView(ListAPIView):
    pagination_class = PaginationSerializer
    serializer_class = ClipSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        resultado = Clip.objects.filter(
          agente__id=self.kwargs['agente'],
          mapa__id=self.kwargs['mapa'],
        ).order_by('-likes')

        return resultado