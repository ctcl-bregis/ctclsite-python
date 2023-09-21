# ctclsite-python - CTCL 2020-2023
# File: views.py
# Purpose: Views for blog
# Created: September 11, 2023
# Modified: September 11, 2023

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.template import loader
from app.lib import loadjson

def menu(request):

    return HttpResponse

def post(request):

    template = loader.get_template("rl_content.html")

    return HttpResponse