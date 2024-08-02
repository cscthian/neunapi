from django.urls import path

from . import views

urlpatterns = [
    path('add-blog/', views.CreateViewBlog.as_view()),
    path('api/portfolio/home/retrive/id/<int:id>/', views.GetHomePortfolio.as_view()),
    path('api/portfolio/skills/list/', views.ListSkills.as_view()),
    path('api/portfolio/blog/list/', views.ListBlog.as_view()),
    path('api/portfolio/blog/retrive/<slug>/', views.RetriveBlogSlug.as_view()),
    path('api/portfolio/experience/list/', views.ListExperiences.as_view()),   
]
