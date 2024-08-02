from django.urls import path
from . import views

urlpatterns = [
  path('api/neun/products-list/', views.ListProductsNeun.as_view(), name='products-list'),
]