# ctclsite-python - CTCL 2020-2023
# File: urls.py
# Purpose: RAMList URLs
# Created: August 27, 2023
# Modified: September 11, 2023

from django.contrib import admin
from django.urls import path, re_path
from . import views

urlpatterns = [
    re_path("(?P<path>.*)$", views.content),
    path("log/", views.log),
]
