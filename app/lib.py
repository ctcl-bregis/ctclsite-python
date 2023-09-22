# ctclsite-python - CTCL 2020-2023
# File: lib.py
# Purpose: Commonly used functions used across the app. Similar to lib.rs in Rust.
# Created: September 11, 2023
# Modified: September 21, 2023

import json
import os

# Function that catches any exception from trying to use print() while headless
def printe(text):
    try:
        print(text)
    except:
        pass

with open("mgmt/config.json") as f:
    global_cfg = json.loads(f.read())["config"]

# Load compiled SCSS file if it exists
if os.path.exists(global_cfg["scss_comp"]):
    with open(global_cfg["scss_comp"]) as f:
        global_css = f.read()
else:
    printe(f"lib.py WARNING: Compiled CSS file {global_cfg['scss_comp']} does not exist")
    global_css = ""

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