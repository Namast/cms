from django.urls import path

from .views import *

urlpatterns = [
    path('<slug:category>/<slug:slug>/', PostDetail.as_view(), name='post_detail'),
    path('<slug:category>/', PostCategory.as_view(), name='post_list_category'),
    path('', PostCategory.as_view()),
]