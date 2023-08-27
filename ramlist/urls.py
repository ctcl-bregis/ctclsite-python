# ctclsite-python - CTCL 2020-2023
# File: urls.py
# Purpose: RAMList URLs
# Created: August 27, 2023
# Modified: August 27, 2023

from django.contrib import admin
from django.urls import path

urlpatterns = [
    #path('admin/', admin.site.urls),
    path("ramlist/<str:page>/", views.list),
    path("ramlist/about/", views.about),
    path("ramlist/log/", views.log),
]
