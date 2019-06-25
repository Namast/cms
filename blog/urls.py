from django.urls import path

from .views import *

urlpatterns = [
    path('<slug:category>/', PostList.as_view()),
    path('post/<int:pk>/', PostDetail.as_view(), name='post_detail'),
    path('', PostList.as_view()),
]