from django.views.generic import ListView, DetailView
from django.shortcuts import render

from .models import BlogPost, Comment
from .forms import CommentForm


class BlogPostListView(ListView):
    # model = BlogPost
    queryset = BlogPost.published.all()
    template_name = "list.html"
    context_object_name = 'blogposts'


class BlogPostDetailView(DetailView):
    model = BlogPost
    template_name = "detail.html"
    context_object_name = 'blogpost'

    def get(self):
        comments = self.model.comments.filter(active=True)
        comment_form = CommentForm()
        pass

    def post(self):
        new_comment = None
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.blogpost = self.model
            new_comment.save()
        pass
