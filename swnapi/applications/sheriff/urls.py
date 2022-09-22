from django.conf.urls import include, url
from django.urls import path, re_path
from . import views

app_name="sheriff_app"

urlpatterns = [
    path(
        'api/sheriff/get/home/', 
        views.GetHomeSheriff.as_view(),
    ),
    path(
        'api/sheriff/list/agentes/', 
        views.AgentesListView.as_view(),
    ),
    path(
        'api/sheriff/list-by-map/agentes/', 
        views.AgentesByMapaListView.as_view(),
    ),
    path(
        'api/sheriff/list/mapas/', 
        views.MapasListView.as_view(),
    ),
    path(
        'api/sheriff/list/clips/<agente>/<mapa>/', 
        views.ClipsListView.as_view(),
    ),
]