from django.shortcuts import render, get_object_or_404
from django.views import View
from django.views.generic import DetailView

from .models import Post


class PostList(View):
    def get(self, request):
        posts = Post.objects.filter(category__published=True)
        return render(request, 'blog/post-list.html', {"post_list": posts})


class PostCategory(View):
    def get(self, request, category):
        posts = Post.objects.filter(category__slug=category, category__published=True)
        if Post.exists():
            return render(request, 'blog/post-list.html', {"post_list": posts})
        else:
            raise Http404


class PostDetail(DetailView):
    def get(self, request, pk):
        post = get_object_or_404(Post, pk=pk)
        return render(request, 'blog/post-detail.html', {'post': post})