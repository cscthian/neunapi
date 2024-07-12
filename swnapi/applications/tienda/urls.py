from django.urls import path
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
    path(
        'api/tienda/categorias/lista/', 
        views.CategoryListView.as_view(),
        name='categorias-lista',
    ),
    path(
        'api/tienda/colores/lista/', 
        views.ColorsListView.as_view(),
        name='colores-lista',
    ),
]
