from django.http import Http404
from django.shortcuts import render, get_object_or_404
from django.views import View

from .models import Post, Category, Comment


class PostList(View):
    def get(self, request, *args, **kwargs):
        posts = Post.objects.filter(category__active=True)
        return render(request, 'blog/post-list.html', {"post_list": posts})


class PostCategory(View):
    def get(self, request, category, *args, **kwargs):
        posts = Post.objects.filter(category__slug=category, category__active=True)
        if posts.exists():
            return render(request, 'blog/post-list.html', {"post_list": posts})
        else:
            raise Http404


class PostDetail(View):
    """Вывод полной статьи"""
    def get(self, request, category, slug):
        post = get_object_or_404(Post, slug=slug)
        comments = Comment.objects.filter(post__slug=slug)
        return render(request, "blog/post-detail.html", {'post': post, 'comments': comments})