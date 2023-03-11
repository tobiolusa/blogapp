from django.shortcuts import render, get_object_or_404
from .models import Post
from django.views import generic
from .form import CommentForm

class PostListView(generic.ListView):
    model = Post
    queryset = Post.objects.filter(status=1).order_by('created_on')
    template_name = 'index.html'
    
class PostDetailView(generic.DetailView):
    model = Post
    template_name = 'post-detail.html'
    def comment_here(request, slug):
        comments = Post.comments.filter(active=True)
        new_comment = None
        if request.method == 'POST':
            comment_form = CommentForm(data=request.POST)
            if comment_form.is_valid():
                new_comment = comment_form.save(commit=False)
                new_comment.post = Post
                new_comment.save()
                
        else:
            comment_form = CommentForm()
        
        return render(request, {'post': Post,
                                           'comments': comments,
                                           'new_comment': new_comment,
                                           'comment_form': comment_form})
        