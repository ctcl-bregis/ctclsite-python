# ctclsite-python - CTCL 2020-2023
# File: urls.py
# Purpose: URLs for the lite version of ctclsite
# Created: December 21, 2023
# Modified: December 21, 2023

from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("", include("lite.about.urls")),
    path("projects/", include("lite.projects.urls")),
    path("blog/", include("lite.blog.urls")),
    #path("ramlist/", include("main.ramlist.urls"))
]