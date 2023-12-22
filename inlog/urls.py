# ctclsite-python - CTCL 2020-2023
# File: inlog/urls.py
# Purpose: URLs for the client-side logging feature
# Created: December 16, 2023
# Modified: December 16, 2023

from django.contrib import admin
from django.urls import include, path
from . import views

urlpatterns = [
    path("", views.incoming),
    path("getip/", views.getip)
]