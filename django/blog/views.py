from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required

from .models import Post
from .forms import PostForm

from django.utils import timezone
from .log import mylog
import logging
import ipdb


@login_required
def post_list(request):
    posts = Post.objects.order_by('created_date').reverse()
    for post in posts:
        post_text_array = post.text.splitlines()
        if len(post_text_array) >= 3:
            post.text = post_text_array[0] + "\n" + post_text_array[1] + "\n" + post_text_array[2]
    logging.debug(post)
    return render(request, 'blog/post_list.html', {'posts': posts})


@login_required
def detail(request, blog_id):
    post = get_object_or_404(Post, pk=blog_id)
    return render(request, 'blog/post_detail.html', {'post': post})


@login_required
def post_draft_list(request):
    posts = Post.object.filter(published_date__isnull=True).order_by('creates_date')
    return render(request, 'blog/post_draft_list.html', {'post': posts})


@login_required
def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid:
            post = form.save(commit=False)
            post.author = request.user
            #post.published_date = timezone.now()
            post.save()
            return redirect('blog:detail', blog_id = post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})


@login_required
def edit(request, blog_id):
    post = get_object_or_404(Post, pk=blog_id)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid:
            post = form.save(commit=False)
            post.author = request.user
            #post.published_date = timezone.now()
            post.save()
            return redirect('blog:detail', blog_id=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})


@login_required
def publishing(request, blog_id):
    blog = get_object_or_404(Post, pk=blog_id)
    blog.publish()
    return redirect('blog:detail')

@login_required
def unpublishing(request, blog_id):
    blog = get_object_or_404(Post, pk=blog_id)
    blog.unpublish()
    return redirect('blog:detail')

@login_required
def post_remove(request, blog_id):
    post = get_object_or_404(Post, pk=blog_id)
    post.delete()
    return redirect('post_list')