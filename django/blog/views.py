from django.shortcuts import render, get_object_or_404
from .models import Post
from django.views import generic
from django.utils import timezone


def post_list(request):
    blogs = Post.objects.order_by('created_date')
    return render(request, 'blog/post_list.html', {'blogs': blogs})

def publishing(request, blog_id):
    blog = get_object_or_404(Post, pk=blog_id)
    blog.publish()
    return post_list(request)

def unpublishing(request, blog_id):
    blog = get_object_or_404(Post, pk=blog_id)
    blog.unpublish()
    return post_list(request)


