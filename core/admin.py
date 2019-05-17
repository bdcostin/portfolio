from django.contrib import admin
from .models import Projects

@admin.register(Projects)
class ProjectsAdmin(admin.ModelAdmin):
    list_display = ('title', 'thumb_nail', 'description', 'deployed_url')
    exclude = ('slug',)
