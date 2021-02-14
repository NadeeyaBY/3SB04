from django.shortcuts import render
from django.utils import timezone
from .models import Post,Photo

def post_list(request):
    posts = Post.objects.all()
    return render(request, 'blog/post_list.html', {'posts': posts})

def photo_list(request):
    # posts = Post.objects.order_by('-created_date')
    return render(request, 'blog/photo_list.html', {})
