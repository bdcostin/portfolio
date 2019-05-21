from django.urls import path
from . import views 

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('projects/', views.ProjectsView.as_view(), name='projects'),
]
