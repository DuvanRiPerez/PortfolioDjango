from django.shortcuts import render, get_object_or_404
from .models import Post

# Create your views here.
def render_posts(requets):
    posts= Post.objects.all()
    return render(requets, 'posts.html', {'posts' : posts})

def post_details(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    return render(request, 'post_detail.html', {"post":post})
