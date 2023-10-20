# ctclsite-python - CTCL 2020-2023
# File: views.py
# Purpose: Views for Projects page
# Created: October 3, 2023
# Modified: October 20, 2023

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.template import loader
from app import lib
from markdown import markdown

page_cfg = lib.loadjson("pages/projects/config.json")
content_dir = "pages/projects/content/"

pages = {}
for cat in page_cfg["cats"].keys():
    for subpage in page_cfg["cats"][cat]["subpages"]:
        pages[subpage["link"]] = subpage

def menu(request):
    template = loader.get_template("projects_menu.html")
    context = lib.mkcontext(page_cfg["menu"])
    context["menu"] = page_cfg["cats"]

    return HttpResponse(template.render(context, request))

def subpage(request, subpagename):
    template = loader.get_template("projects_content.html")
    context = lib.mkcontext(pages[subpagename])
    with open(content_dir + pages[subpagename]["content"]) as f:
        context["rendered"] = markdown(f.read())

    return HttpResponse(template.render(context, request))