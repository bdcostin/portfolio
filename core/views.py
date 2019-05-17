from django.shortcuts import render
from django.views.generic import TemplateView, ListView

# Create your views here.

class IndexView(TemplateView):
    template_name = "index.html"
    
class ProjectsView(ListView):
    template_name = "projects.html"
