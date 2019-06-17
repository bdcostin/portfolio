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
    technology = models.CharField(max_length=200)
    deployed_url = models.CharField(max_length=150, null=True, blank=True)
    github_url = models.CharField(max_length=150, null=True, blank=True)
    slug = models.SlugField(unique=True)

    class Meta:
        ordering = ['-title']

    def set_slug(self):
        '''Creates a unique slug for every project'''
        if self.slug:
            return
        base_slug = slugify(self.title)

        slug = base_slug
        n = 0

        while User.objects.filter(slug=slug).count():
            n += 1
            slug = base_slug + '-' + str(n)
        
        self.slug = slug
    
    def save(self, *args, **kwargs):
        '''Hides slug field in admin and saves slug to use in url'''
        self.set_slug()
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("project-detail", args=[str(self.slug)])
    
    def __str__(self):
        return self.title
