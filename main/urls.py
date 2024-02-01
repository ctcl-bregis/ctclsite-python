# ctclsite-python - CTCL 2020-2024
# File: urls.py
# Purpose: URLs for the main version of ctclsite
# Created: November 21, 2023
# Modified: January 7, 2024

from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("", include("main.about.urls")),
    path("services/", include("main.services.urls")),
    path("projects/", include("main.projects.urls")),
    path("blog/", include("main.blog.urls")),
    path("bcc_cc/", include("main.bcc_cc.urls"))
    #path("ramlist/", include("main.ramlist.urls"))
] 