# ctclsite-python - CTCL 2020-2023
# File: views.py
# Purpose: Views for "about"
# Created: August 30, 2023
# Modified: September 2, 2023

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.template import loader

def main(request):
    template = loader.get