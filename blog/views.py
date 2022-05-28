from django.views.generic import ListView, DetailView
from django.shortcuts import render

from .models import BlogPost


class BlogPostListView(ListView):
    model = BlogPost
    template_name = "blog/list.html"
    context_object_name = 'blogposts'


class BlogPostDetailView(DetailView):
    model = BlogPost
    template_name = "blog/detail.html"
    context_object_name = 'blogpost'
