from django.urls import path

from .views import *


urlpatterns = [
    path('<slug:slug>/', LinkMenu.as_view(), name="menu_link")
]