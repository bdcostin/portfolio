from django.urls import path
from . import views 

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('resume/', views.ResumeView.as_view(), name='resume'),
    path('projects/', views.ProjectsView.as_view(), name='projects'),
    path('<slug:slug>/', views.ProjectDetailView.as_view(), name='project-detail'),
]
