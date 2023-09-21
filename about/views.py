# ctclsite-python - CTCL 2020-2023
# File: views.py
# Purpose: Views for "about"
# Created: August 30, 2023
# Modified: September 21, 2023

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.template import loader
from app import lib

about_cfg = lib.loadjson("about/config.json")["config"]

def main(request):
    template = loader.get_template("about_main.html")


    context = lib.mkcontext(about_cfg["root"]["themecolor"], "CTCL Website")
    return HttpResponse(template.render(context, request))

def pp(request):
    template = loader.get_template("about_md.html")

    return HttpResponse(template.render())

def licensing(request):
    template = loader.get_template("about_md.html")