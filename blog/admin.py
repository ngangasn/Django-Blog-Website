from django.contrib import admin

from .models import BlogPost


@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    list_display: ('post_title', 'created_on', 'published_on', 'meta_description')
    prepopulated_fields = {'slug': ('post_title',), }