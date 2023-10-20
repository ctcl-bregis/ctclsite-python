# ctclsite-python - CTCL 2020-2023
# File: urls.py
# Purpose: App URLs
# Created: August 26, 2023
# Modified: October 7, 2023

from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    #path('admin/', admin.site.urls),
    path("", include("pages.about.urls")),
    path("projects/", include("pages.projects.urls")),
    path("blog/", include("pages.blog.urls")),
    #path("ramlist/", include("pages.ramlist.urls"))
]
