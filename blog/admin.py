from django.contrib import admin

from .models import BlogPost, Comment


@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('post_title', 'author', 'published_on', 'status')
    prepopulated_fields = {'slug': ('post_title',), }


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('username', 'user_email', 'blogpost', 'active')
    list_filter = ('active', )
    search_fields = ('username', 'user_email', 'comment')
