# ctclsite-python - CTCL 2020-2023
# File: lib.py
# Purpose: Commonly used functions used across the app. Similar to lib.rs in Rust.
# Created: September 11, 2023
# Modified: December 14, 2023

import json
import os

# Function that catches any exception from trying to use print() while headless
def printe(text):
    try:
        print(text)
    except:
        pass

# Global configuration
with open("config/config.json") as f:
    global_cfg = json.loads(f.read())["config"]

if os.path.exists(global_cfg["main_scss_comp"]):
    with open(global_cfg["main_scss_comp"]) as f:
        main_css = json.loads(f.read())
else:
    printe(f"lib.py WARNING: Compiled CSS file {global_cfg['main_scss_comp']} does not exist")
    main_css = ""

if os.path.exists(global_cfg["lite_scss_comp"]):
    with open(global_cfg["lite_scss_comp"]) as f:
        lite_css = json.loads(f.read())
else:
    printe(f"lib.py WARNING: Compiled CSS file {global_cfg['lite_scss_comp']} does not exist")
    lite_css = ""

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
        jsoncontent = json.loads(filecontent)["config"]
    except Exception as err:
        printe(f"lib.py ERROR: Exception {err} raised")
        return None

    return jsoncontent

# Function for pre-filling a dictionary used as the context for templates
def mkcontext(subpageindex, lite = False):
    context = subpageindex
    theme = subpageindex["theme"]
    if lite:
        try:
            context["styling"] = lite_css[theme]
        except:
            printe(f"lib.py WARNING: Theme \"{theme}\" not found, defaulting to \"gold\"")
            context["styling"] = lite_css["gold"]
    else:
        try:
            context["styling"] = main_css[subpageindex["theme"]]
        except:
            printe(f"lib.py WARNING: Theme \"{theme}\" not found, defaulting to \"gold\"")
            context["styling"] = main_css["gold"]

    return context

def getthemecolors():
    colors = {}
    fgcolors = {}
    for key, value in global_cfg["styling_colors"].items():
        colors[key] = value["color"]
        fgcolors[key] = value["fgcolor"]

    return (colors, fgcolors)