# ctclsite-python - CTCL 2020-2024
# File: urls.py
# Purpose: Services URLs
# Created: January 7, 2024
# Modified: January 7, 2024

from django.contrib import admin
from django.urls import include, path
from . import views

urlpatterns = [
    path("", views.main)
]
