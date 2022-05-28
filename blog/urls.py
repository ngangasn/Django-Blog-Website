from django.urls import path

from .views import BlogPostListView, BlogPostDetailView


urlpatterns = [
    path('', BlogPostListView.as_view(), name='blogposts'),
    path('<str:slug>/', BlogPostDetailView.as_view(), name='blogpost'),
]
