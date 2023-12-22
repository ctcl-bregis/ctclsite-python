# ctclsite-python - CTCL 2020-2023
# File: urls.py
# Purpose: URLs for projects page
# Created: December 21, 2023
# Modified: December 21, 2023

from django.contrib import admin
from django.urls import include, path
from . import views

urlpatterns = [
    path("", views.menu),
    path("<str:subpagename>/", views.subpage)
]