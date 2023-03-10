from django.shortcuts import render
from .models import Post
from django.views import generic

class PostListView(generic.ListView):
    model = Post
    queryset = Post.objects.filter(status=1).order_by('created_on')
    template_name = 'index.html'
    
class PostDetailView(generic.DetailView):
    model = Post
    template_name = 'post-detail.html'