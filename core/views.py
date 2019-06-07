from django.shortcuts import render, render_to_response
from django.views.generic import TemplateView, ListView
from core.models import Project
from django.http import HttpResponse 
from .forms import ContactForm 

# Create your views here.

class IndexView(ListView):
    model = Project
    queryset = Project.objects.order_by('-title')
    template_name = "index.html"
    context_object_name = 'project_list'

class ProjectsView(ListView):
    template_name = "projects.html"

def contact_me(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # send email code goes here
            return HttpResponse('Thanks for contacting me!')
    else:
        form = ContactForm()

    return render(request, 'contact-me.html', {'form': form})

class ResumeView(TemplateView):
    template_name = "resume.html"
