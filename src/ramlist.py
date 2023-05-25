# ctclsite-python - CTCL 2020-2023
# May 15, 2023 - May 25, 2023
# Purpose: RAMList Flask Blueprint

from flask import Blueprint, render_template, abort, request
from src.lib import getpageinfo, csvfile2list, md2html
import csv

rl_bp = Blueprint('rl_bp', __name__, template_folder='templates')

# Lists config prefix
rlcfg = "config/ramlist/lists/"
rllogcfg = "config/ramlist/log/"

# Global table width
table_width = "2200pt"

# Load menu and page index on startup instead of every page load
menu = csvfile2list("config/ramlist/menu.csv")
pageindex = csvfile2list("config/ramlist/index.csv")

lists = []
for i in pageindex:
    if i["type"] == "list":
        lists.append(i["page"])

# Load and process all list CSV files on server startup        
listscontents = {}
for i in lists:
    for x in pageindex:
        if x["page"] == i:
            pagedict = x
            break
    else:
        raise Exception
        
    vindex = csvfile2list(pagedict["content"])
    tindex = csvfile2list(pagedict["rltableinfo"])
        
    header_keys = [i["ydata"] for i in tindex]

    vendors = {}
    brands = []
    count = 0
    for v in vindex: 
        csvfile = v["file"]
        vendors[v["brand"]] = csvfile2list(f"{rlcfg}{i}/{csvfile}")
        count += len(vendors[v["brand"]])
        brands.append(v["brand"])
    memtypes = listscontents.keys
    
    listscontents[i] = vendors
    listscontents[i]["brands"] = brands
    listscontents[i]["header_keys"] = header_keys
    listscontents[i]["tindex"] = tindex
    listscontents[i]["count"] = count

# RAMList menu
@rl_bp.route("/")
def index():
    return render_template("rl_menu.jinja2", menu = menu, pageinfo = getpageinfo("ramlist", "root"))

# Everything but the menu
@rl_bp.route("/<page>/")
def subpage(page):
    for i in pageindex:
        if i["page"] == page:
            pagedict = i
            break
    else:
        abort(404)
    
    if pagedict["type"] == "list":
        listcontents = listscontents[page]
        return render_template("rl_list.jinja2", pageinfo = getpageinfo("ramlist", page), table_width = table_width, listcontents = listcontents)
    elif pagedict["type"] == "log":
        posts = csvfile2list(pagedict["content"])
        content = []
        # TODO: Make this more efficient, idea: convert md to html on server startup instead of every page load
        for i in posts:
            html = md2html(rllogcfg + i["path"])
            post = {"date": i["date"], "content": html}
            content.append(post)
            
        return render_template("rl_log.jinja2", content = content, pageinfo = getpageinfo("ramlist", page))
    elif pagedict["type"] == "markdown":
        content = md2html(pagedict["content"])
            
        return render_template("rl_about.jinja2", content = content, pageinfo = getpageinfo("ramlist", page))
    else:
        raise Exception("Page type unknown")
