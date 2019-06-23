from django.urls import path
from . import views 

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('about/', views.AboutView.as_view(), name='about'),
    path('projects/', views.ProjectsView.as_view(), name='projects'),
    path('<slug:slug>/', views.ProjectDetailView.as_view(), name='project-detail'),
]
