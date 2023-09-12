# ctclsite-python - CTCL 2020-2023
# File: views.py
# Purpose: RAMList views
# Created: August 31, 2023
# Modified: September 11, 2023

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.template import loader
from app.lib import loadjson

ramlist_cfg = loadjson("ramlist/config.json")

# Any content page
def content(request):
    template = loader.get_template("rl_content.html")

    print(ramlist_cfg)

    return HttpResponse(template.render(context, request))

# Announcements page
def log(request):
    template = loader.get_template("rl_log.html")

    return HttpResponse(template.render(context, request))