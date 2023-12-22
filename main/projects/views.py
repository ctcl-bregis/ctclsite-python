# ctclsite-python - CTCL 2020-2023
# File: views.py
# Purpose: Views for Projects page
# Created: October 3, 2023
# Modified: December 22, 2023

from django.template.defaulttags import register
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseNotFound
from django.shortcuts import render
from django.template import loader
from app import lib
from markdown import markdown

page_cfg = lib.loadjson("config/projects/config.json")
content_dir = "config/projects/"

pages = {}
for cat in page_cfg["cats"].keys():
    for subpage in page_cfg["cats"][cat]["subpages"]:
        pages[subpage["link"]] = subpage

@register.filter
def get_item(dictionary, key):
    return dictionary.get(key)

def menu(request):
    template = loader.get_template("main/projects_menu.html")
    context = lib.mkcontext(page_cfg["menu"])
    context["menu"] = page_cfg["cats"]

    context["fgcolors"] = lib.getthemecolors()[1]
    context["colors"] = lib.getthemecolors()[0]

    return HttpResponse(template.render(context, request))

def subpage(request, subpagename):
    template = loader.get_template("main/projects_content.html")

    if subpagename in pages:
        context = lib.mkcontext(pages[subpagename])
        with open(content_dir + pages[subpagename]["content"]) as f:
            context["rendered"] = markdown(f.read())
    else:
        return HttpResponseNotFound()

    return HttpResponse(template.render(context, request))