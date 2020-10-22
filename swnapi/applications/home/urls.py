from django.conf.urls import include, url
from django.urls import path, re_path
from . import views

app_name="home_app"

urlpatterns = [
    path(
        '', 
        views.HomeView.as_view(),
        name='index',
    ),
    path(
        'servicio/<pk>/', 
        views.ServiciosDetailView.as_view(),
        name='servicios-detail',
    ),
]
