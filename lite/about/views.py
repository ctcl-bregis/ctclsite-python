# ctclsite-python - CTCL 2020-2023
# File: views.py
# Purpose: Views for "about"
# Created: December 21, 2023
# Modified: December 21, 2023

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.template import loader
from app import lib
from markdown import markdown

page_cfg = lib.loadjson("config/about/config.json")

def main(request):
    template = loader.get_template("lite/about_main.html")
    context = lib.mkcontext(page_cfg["root"], lite = True)

    context["sections"] = page_cfg["root"]["sections"]

    for section in context["sections"]:
        try:
            with open(section["content"]) as f:
                mdsource = f.read()

            try:
                section["rendered"] = markdown(mdsource)
            except Exception as err:
                section["rendered"] = f"<i>Markdown rendering failed: {err}</i>"

        except Exception as err:
            section["rendered"] = f"<i>File operation error when opening {section['content']}</i>"

    return HttpResponse(template.render(context, request))

def pp(request):
    template = loader.get_template("lite/about_md.html")
    context = lib.mkcontext(page_cfg["privacy"], lite = True)

    try:
        with open(page_cfg["privacy"]["content"]) as f:
            mdsource = f.read()

        try:
            context["rendered"] = markdown(mdsource)
        except Exception as err:
            context["rendered"] = f"<i>Markdown rendering failed: {err}</i>"

    except Exception as err:
        context["rendered"] = f"<i>File operation error when opening {page_cfg['licensing']['content']}</i>"

    return HttpResponse(template.render(context, request))

def licensing(request):
    template = loader.get_template("lite/about_md.html")
    context = lib.mkcontext(page_cfg["licensing"], lite = True)

    try:
        with open(page_cfg["licensing"]["content"]) as f:
            mdsource = f.read()

        try:
            context["rendered"] = markdown(mdsource)
        except Exception as err:
            context["rendered"] = f"<i>Markdown rendering failed: {err}</i>"

    except Exception as err:
        context["rendered"] = f"<i>File operation error when opening {page_cfg['licensing']['content']}</i>"

    return HttpResponse(template.render(context, request))