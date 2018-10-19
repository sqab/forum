from django.utils import timezone
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required

from .models import Post, CommentPost, Like, Hit
from .forms import PostForm, CommentForm


@login_required
def feed(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    context = {
        'posts': posts
    }
    return render(request, 'blog/feed.html', context)


@login_required
def details(request, pk):
    post = get_object_or_404(Post, pk=pk)
    comments = CommentPost.objects.filter(post=post)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = request.user
            comment.post = post
            comment.save()
    else:
        form = CommentForm()
    likes = Like.objects.filter(post_id=pk)
    new_view = Hit.objects.get_or_create(user=request.user, post_id=pk)
    views = Hit.objects.filter(post_id=pk)
    context = {
        "post": post,
        "form": form,
        'comments': comments,
        'likes': likes.count,
        'views': views.count
    }
    return render(request, "blog/details.html", context)


@login_required
def new_post(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('details', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/new_post.html', {'form': form})


def like(request, pk):
    new_like, created = Like.objects.get_or_create(user=request.user, post_id=pk)
    post = Post.objects.get(pk=pk)
    if not created:
        like = Like.objects.get(user=request.user, post_id=pk).delete()
    return redirect('details', pk=pk)


def posts_by_user(request, pk):
    posts = Post.objects.filter(user_id=pk)
    user = User.objects.get(id=pk)
    context = {
        'posts': posts,
        'user': user
    }
    return render(request, 'blog/posts_by_user.html', context)


@login_required
def profile(request):
    user = User.objects.filter(id=request.user.id)
    context = {
        'user': user
    }
    return render(request, 'profile/profile.html', context)
