from rest_framework.routers import DefaultRouter
#
from . import viewsets

router = DefaultRouter()

router.register(r'api/cursos', viewsets.CursoViewSet, basename='curso')

urlpatterns = router.urls