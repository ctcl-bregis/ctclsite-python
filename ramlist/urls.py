# ctclsite-python - CTCL 2020-2023
# File: urls.py
# Purpose: RAMList URLs
# Created: August 27, 2023
# Modified: September 11, 2023

from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("", views.content),
    path("<str:page>/", views.content),
    path("log/", views.log),
]
