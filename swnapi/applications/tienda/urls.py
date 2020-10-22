from django.conf.urls import include, url
from django.urls import path, re_path
from . import views

app_name="tienda_app"

urlpatterns = [
    path(
        'api/tienda/producto/<id>/', 
        views.ProductDetailViewSet.as_view(),
        name='producto-detail',
    ),
    path(
        'api/tienda/productos/lista/', 
        views.ProductListView.as_view(),
        name='producto-lista',
    ),
]
