# ctclsite-python - CTCL 2020-2023
# File: urls.py
# Purpose: App URLs
# Created: August 26, 2023
# Modified: December 21, 2023

from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    #path('admin/', admin.site.urls),
    path("", include("main.urls")),
    path("lite/", include("lite.urls")),
    path("inlog/", include("inlog.urls"))
]
