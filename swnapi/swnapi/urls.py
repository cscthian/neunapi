"""
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
#
from applications.home.views import Error404View, Error505View

urlpatterns = [
    path('administrar/', admin.site.urls),
    path('', include('applications.tienda.urls'), name="tienda"),
    path('', include('applications.neun.urls'), name='neun'),
    path('', include('applications.home.urls'), name="home"),
    path('', include('applications.examen.urls'), name="examen"),
    path('', include('applications.sheriff.urls'), name="sheriff"),
    path('', include('applications.portfolio.urls'), name="portfolio"),

    path('', include('applications.cursos.routes')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler404 = Error404View.as_view()

handler500 = Error505View.as_error_view()