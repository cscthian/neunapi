
from django.shortcuts import render
#
from rest_framework import viewsets, generics
#
from rest_framework.authtoken.models import Token
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
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
    ProductSerializer,
    CategorySerializer,
    ColorsSerializer,
    PaginationSerializer
)
#
from .models import Product, Category, Colors


class ProductDetailViewSet(RetrieveAPIView):
    lookup_field = 'pk' 
    permission_classes = (AllowAny,)
    serializer_class = ProductSerializer
    queryset = Product.objects.filter(publicado=True)

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        new_visits =  instance.visits + 1
        #
        Product.objects.filter(pk=instance.id).update(visits=new_visits)
        serializer = self.get_serializer(instance)
        return Response(serializer.data)


class ProductListView(ListAPIView):
    pagination_class = PaginationSerializer
    permission_classes = (AllowAny,)
    serializer_class = ProductSerializer

    def get_queryset(self):
        queryset = Product.objects.por_categoria(
            name = self.request.query_params.get('name', ''),
            category = self.request.query_params.get('category', ''),
            colors = self.request.query_params.get('colors', []),
            order = self.request.query_params.get('order', 'populares'),
        )

        return queryset