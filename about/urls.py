# ctclsite-python - CTCL 2020-2023
# File: urls.py
# Purpose: About/home URLs
# Created: August 30, 2023
# Modified: August 31, 2023

from django.contrib import admin
from django.urls import include, path
from . import views

urlpatterns = [
    path("/", views.main),
    path("/privacy/", views.pp),
    path("/licensing/", views.licensing)
]
