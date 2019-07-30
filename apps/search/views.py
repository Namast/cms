from django.shortcuts import render
from django.views import View
from django.db.models import Q

from blog.models import Post


class SearchView(View):
    """Поиск статей"""
    def get(self, request, *args, **kwargs):
        search = request.GET.get("q", None)
        posts = Post.objects.filter(Q(title__icontains=search) |
                                    Q(text__icontains=search))
        return render(request, "search/search.html", {"post_list": posts})


