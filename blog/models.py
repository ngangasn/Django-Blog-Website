from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User


class BlogPostPublishedManager(models.Manager):
    def get_queryset(self):
        return super(BlogPostPublishedManager, self).get_queryset().filter(status="Published")


class BlogPost(models.Model):

    STATUS_CHOICES = [
        ('DRAFT', 'Draft'),
        ('PUBLISHED', 'Published'),
    ]

    post_title = models.CharField(max_length=90)
    slug = models.SlugField(max_length=90)
    meta_description = models.CharField(max_length=1000)
    content = models.TextField()
    featured_image = models.ImageField(upload_to='blog/images', null=True, blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    published_on = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='DRAFT')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blogposts')

    class Meta:
        ordering = ('-published_on', )
    
    def __str__(self):
        return self.post_title

    def get_absolute_url(self):
        return reverse("blogpost", args={str(self.slug)})

    objects = models.Manager()
    published = BlogPostPublishedManager()


class Comment(models.Model):
    blogpost = models.ForeignKey(BlogPost, on_delete=models.CASCADE, related_name='comments')
    username = models.CharField(max_length=100)
    user_email = models.EmailField()
    comment = models.TextField(max_length=5000)
    comment_initiated_on = models.DateTimeField(auto_now_add=True)
    comment_updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=False)

    class Meta:
        ordering = ('-comment_initiated_on', )

    def __str__(self):
        return f'{self.username}\'s commented on {self.blogpost}'
