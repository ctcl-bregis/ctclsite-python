# ctclsite-python - CTCL 2020-2024
# File: views.py
# Purpose: Services views
# Created: January 7, 2024
# Modified: January 7, 2024

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.template import loader
from app import lib
from markdown import markdown

page_cfg = lib.loadjson("config/services/config.json")

def main(request):
    template = loader.get_template("lite/services_main.html")
    context = lib.mkcontext(page_cfg["root"], lite=True)

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