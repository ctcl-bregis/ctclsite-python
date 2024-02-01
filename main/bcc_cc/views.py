# ctclsite-python - CTCL 2020-2024
# File: views.py
# Purpose: Brightpoint Computer Club views
# Created: January 31, 2024
# Modified: January 31, 2024

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.template import loader
from app import lib
from markdown import markdown

page_cfg = lib.loadjson("config/bcc_cc/config.json")

# General replacement for the Linktree page
def main(request):
    template = loader.get_template("main/bcc_cc.html")
    context = lib.mkcontext(page_cfg["main"])
    

    return HttpResponse(template.render(context, request))