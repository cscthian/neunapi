from django.urls import path
from . import views

app_name="examen_app"

urlpatterns = [
    path(
        'api/test/category/list/', 
        views.QuestionListView.as_view(),
        name='questions-list',
    ),
]