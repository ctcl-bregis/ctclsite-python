# ctclsite-python - CTCL 2020-2023
# File: urls.py
# Purpose: URLs for the main version of ctclsite
# Created: November 21, 2023
# Modified: November 21, 2023

from django.contrib import admin
from django.urls import include, path
from . import views

urlpatterns = [
    path("", include("main.about.urls")),
    path("projects/", include("main.projects.urls")),
    path("blog/", include("main.blog.urls")),
    #path("ramlist/", include("pages.ramlist.urls"))
]