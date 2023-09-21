# ctclsite-python - CTCL 2020-2023
# File: lib.py
# Purpose: Commonly used functions used across the app. Similar to lib.rs in Rust.
# Created: September 11, 2023
# Modified: September 21, 2023

import json
import os

with open("app/styling.css") as f:
    globalcss = f.read()

# Function that catches any exception from trying to use print() while headless
def printe(text):
    try:
        print(text)
    except:
        pass

# Load JSON file and return the loaded data
def loadjson(path):
    if not os.path.exists(path):
        printe(f"lib.py ERROR: {path} does not exist")
        return None
    elif os.path.isdir(path):
        printe(f"lib.py ERROR: {path} is a directory")
        return None

    with open(path) as f:
        filecontent = f.read()

    try:
        jsoncontent = json.loads(filecontent)
    except Exception as err:
        printe(f"lib.py ERROR: Exception {err} raised")
        return None

    return jsoncontent

def mkcontext(themecolor, title):
    context = {}

    context["color"] = themecolor
    context["title"] = title
    context["styling"] = globalcss

    return context