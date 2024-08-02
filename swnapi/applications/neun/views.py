from django.shortcuts import render
from django.db.models import Case, When, Value, IntegerField
# drf
from rest_framework.generics import ListAPIView
from rest_framework.authentication import TokenAuthentication, SessionAuthentication
from rest_framework.permissions import IsAuthenticated
#
from .serialziers import ProductosSerializers
from .models import Products


class ListProductsNeun(ListAPIView):
    serializer_class = ProductosSerializers
    permission_classes = [IsAuthenticated,]
    authentication_classes = [TokenAuthentication, SessionAuthentication]

    def get_queryset(self):
        tag = self.request.query_params.get('tag', '')
        results = Products.objects.filter(
            publicado=True,
        ).annotate(
            pripority=Case(
                When(tag__icontains=tag, then=Value(1)),
                default=Value(0),
                output_field=IntegerField()
            )
        ).order_by('-pripority')

        return results

