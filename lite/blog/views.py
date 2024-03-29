# ctclsite-python - CTCL 2020-2023
# File: views.py
# Purpose: Views for blog
# Created: December 21, 2023
# Modified: December 22, 2023

from django.http import HttpResponse, HttpResponseRedirect, HttpResponseNotFound
from django.shortcuts import render
from django.template import loader
from app import lib
from markdown import markdown

content_dir = "config/blog/content/"

page_cfg = lib.loadjson("config/blog/config.json")

def menu(request):
    template = loader.get_template("lite/blog_menu.html")
    context = lib.mkcontext(page_cfg["menu"], lite = True)
    context["posts"] = page_cfg["posts"]

    return HttpResponse(template.render(context, request))

def post(request, postid):
    template = loader.get_template("lite/blog_post.html")

    if postid in page_cfg["posts"]:
        context = lib.mkcontext(page_cfg["posts"][postid], lite = True)
    else:
        return HttpResponseNotFound()

    with open(content_dir + page_cfg["posts"][postid]["content"]) as f:
        mdsource = f.read()

    context["rendered"] = markdown(mdsource)

    return HttpResponse(template.render(context, request))