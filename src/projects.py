# ctclsite-python - CTCL 2020-2023
# May 18, 2023 - May 25, 2023
# Purpose: Projects Flask Blueprint

from flask import Blueprint, render_template, abort
from src.lib import getpageinfo, csvfile2list, md2html

projects_bp = Blueprint('projects_bp', __name__, template_folder='templates')

pageindex = csvfile2list("config/pagemeta.csv")

for i in pageindex:
    if i["page"] == "projects":
        subpageindex = csvfile2list(i["index"])

# Projects List Page
@projects_bp.route("/")
def index():
    return render_template("projects_menu.jinja2", pageinfo = getpageinfo("projects", "root"), pages = subpageindex)

# Projects Content Page
@projects_bp.route("/<page>/")
def projectpage(page):
    for i in subpageindex:
        if i["page"] == page:
            content = i["content"]
            break
    
    content = md2html(content)
    
    return render_template("projects_page.jinja2", pageinfo = getpageinfo("projects", page), content = content)
