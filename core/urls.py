from django.urls import path
from . import views 

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('projects/', views.ProjectsView.as_view(), name='projects'),
    # path('<slug:slug>/', views.project_detail, name='project_detail'),
    path('<slug:slug>/', views.ProjectDetailView.as_view(), name='project-detail'),
    path('resume/', views.ResumeView.as_view(), name='resume'),
]
