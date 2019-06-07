from django.db import models
from django.utils.text import slugify
from django.urls import reverse

class Project(models.Model):
    '''
    This model represents my projects
    '''
    title = models.CharField(max_length=150, null=True, blank=True)
    thumb_nail = models.ImageField(upload_to='static/img/projects', blank=True)
    description = models.TextField(max_length=2000, null=True, blank=True)
    technology = models.CharField(max_length=200)
    deployed_url = models.CharField(max_length=150, null=True, blank=True)
    slug = models.SlugField()

    class Meta:
        ordering = ['-title']

    def set_slug(self):
        '''
        Creates a unique slug for every post
        '''
        if self.slug:
            return
          
    def save(self, *args, **kwargs):
        '''
        Hides slug field in admin- saves slug to use in url
        '''
        self.set_slug()
        super().save(*args, **kwargs)
        
    def get_absolute_url(self):
        return reverse('projects', kwargs={'slug': self.slug})

    def __str__(self):
        return self.title
