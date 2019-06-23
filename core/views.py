from django.views.generic import TemplateView, ListView, DetailView
from core.models import Project 

class IndexView(ListView):
    model = Project
    queryset = Project.objects.order_by('-title')
    paginate_by = 3
    template_name = 'core/index.html'

class ProjectsView(ListView):
    model = Project
    queryset = Project.objects.order_by('-title')
    template_name = 'core/projects.html'

class AboutView(TemplateView):
    template_name = 'core/about.html'

class ProjectDetailView(DetailView):
    model = Project
    template = 'project_detail.html'
    slug_field = 'title'
