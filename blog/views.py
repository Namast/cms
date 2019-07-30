from django.conf import settings
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import Http404
from django.shortcuts import render, get_object_or_404, redirect, get_list_or_404
from django.views import View
from django.views.generic import ListView, DetailView, CreateView


from .models import Post, Comment, Tag
from .forms import CommentForm


class PostCategory(ListView):
    """Вывод статей"""
    model = Post
    template_name = "blog/post-list.html"
    context_object_name = "post_list"

    def get_queryset(self):
        if self.kwargs.get("category") is not None:
            posts = Post.objects.filter(category__slug=self.kwargs.get("category"), category__active=True)
            if posts.exists():
                self.template_name = posts.first().category.template
            else:
                raise Http404
        else:
            posts = Post.objects.filter(category__active=True)
        if not posts.exists():
            raise Http404
        return posts


# class PostList(View):
#     """Вывод списка статей"""
#     def get(self, request, *args, **kwargs):
#         posts = Post.objects.filter(category__active=True)
#         return render(request, 'blog/post-list.html', {"post_list": posts})


# class PostCategory(View):
#     def get(self, request, category, *args, **kwargs):
#         posts = Post.objects.filter(category__slug=category, category__active=True)
#         if posts.exists():
#             return render(request, 'blog/post-list.html', {"post_list": posts})
#         else:
#             raise Http404


# class PostList(ListView):
#     """Вывод списка статей"""
#     model = Post
#     queryset = Post.objects.filter(category__active=True)
#     template_name = "blog/post-list.html"
#     context_object_name = "post_list"


class PostDetail(DetailView, CreateView):
    """Вывод полной статьи"""
    model = Post
    template_name = "blog/post-detail.html"
    context_object_name = "post"
    form_class = CommentForm
#   success_url = '/'

    def form_valid(self, form):
        form.instance.post = Post.objects.get(slug=self.kwargs.get('slug'))
        form.instance.user = self.request.user
        form.save()
        messages.add_message(self.request, settings.MY_INFO, "Ваш комментарий отправлен на проверку, спасибо")
#       self.success_url = reverse_lazy("post_detail", kwargs={"category": self.category.slug, "slug": self.slug})
        self.success_url = form.instance.post.get_absolute_url()
        return super().form_valid(form)


# class PostDetail(View):
#     """Вывод полной статьи"""
#     def get(self, request, category, slug):
#         post = get_object_or_404(Post, slug=slug)
#         form = CommentForm()
#         return render(request, "blog/post-detail.html", {'post': post, "form": form})
#
#     def post(self, request, category, slug):
#         form = CommentForm(request.POST)
#         if form.is_valid():
#             form = form.save(commit=False)
#             form.post = Post.objects.get(slug=slug)
#             form.user = request.user
#             form.save()
#             messages.add_message(request, settings.MY_INFO, "Ваш комментарий отправлен на проверку, спасибо")
#         else:
#             messages.add_message(request, settings.MY_INFO, "Ошибка")
#             return redirect(request.path)


class TagListView(ListView):
    model = Post
    template_name = 'blog/tag-list.html'
    context_object_name = "tag"

    def get_queryset(self):
        return Tag.objects.get(slug=self.kwargs['slug'])
