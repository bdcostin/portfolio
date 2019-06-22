from django.db import models
from django.utils.text import slugify
from django.urls import reverse

class Project(models.Model):
    '''
    This model represents my projects
    '''
    title = models.CharField(max_length=150, null=True, blank=True)
    thumb_nail = models.ImageField(upload_to='uploads/static/img/projects', blank=True)
    description = models.TextField(max_length=2000, null=True, blank=True)
    deployed_url = models.CharField(max_length=150, null=True, blank=True)
    github_url = models.CharField(max_length=150, null=True, blank=True)
    technology = models.CharField(max_length=200, null=True, blank=True)
    slug = models.SlugField(unique=True)
    python = models.BooleanField(default=False)
    django = models.BooleanField(default=False)
    javascript = models.BooleanField(default=False)
    jquery = models.BooleanField(default=False)
    react = models.BooleanField(default=False)
    html = models.BooleanField(default=False)
    css = models.BooleanField(default=False)
    postgresql = models.BooleanField(default=False)
    heroku = models.BooleanField(default=False)
    aws = models.BooleanField(default=False)

    class Meta:
        ordering = ['-title']

    def set_slug(self):
        '''Creates a unique slug for every project'''
        if self.slug:
            return
        slug = slugify(self.title)
        self.slug = slug
    
    def save(self, *args, **kwargs):
        '''Hides slug field in admin and saves slug to use in url'''
        self.set_slug()
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("project-detail", args=[str(self.slug)])
    
    def __str__(self):
        return self.title
