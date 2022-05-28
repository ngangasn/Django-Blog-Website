from django.db import models
from django.urls import reverse


class BlogPost(models.Model):

    STATUS_CHOICES = [
        ('DRAFT', 'Draft'),
        ('PUBLISHED', 'Published'),
    ]

    post_title = models.CharField(max_length=90)
    slug = models.SlugField()
    meta_description = models.CharField(max_length=1000)
    content = models.TextField()
    featured_image = models.ImageField(upload_to='blog/images')
    created_on = models.DateTimeField(auto_now_add=True)
    published_on = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='DRAFT')

    class Meta:
        ordering = ('-published_on', )
    
    def __str__(self):
        return self.post_title

    def get_absolute_url(self):
        return reverse("blogpost", args={str(self.slug)})
    