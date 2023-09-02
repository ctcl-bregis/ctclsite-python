# ctclsite-python - CTCL 2020-2023
# File: urls.py
# Purpose: App URLs
# Created: August 26, 2023
# Modified: August 30, 2023

from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    #path('admin/', admin.site.urls),
    path("about/", include("about.urls")),
    path("blog/", include("blog.urls")),
    path("ramlist/", include("ramlist.urls"))
]
