# ctclsite-python - CTCL 2020-2023
# File: urls.py
# Purpose: URLs for the more accessible version of ctclsite
# Created: November 21, 2023
# Modified: November 21, 2023

from django.contrib import admin
from django.urls import include, path
from . import views

urlpatterns = [
    path("", include("lite.about.urls")),
    path("projects/", include("lite.projects.urls")),
    path("blog/", include("lite.blog.urls")),
    #path("ramlist/", include("lite.ramlist.urls"))
]