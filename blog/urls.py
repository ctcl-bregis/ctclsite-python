# ctclsite-python - CTCL 2020-2023
# File: urls.py
# Purpose: URLs for blog
# Created: September 11, 2023
# Modified: September 19, 2023

from django.contrib import admin
from django.urls import include, path
from . import views

urlpatterns = [
    #path('admin/', admin.site.urls),
    path("", views.menu),
    path("post/<str:postid>/", views.post)
]