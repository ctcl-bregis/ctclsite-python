# ctclsite-python - CTCL 2020-2023
# May 15, 2023 - May 25, 2023
# Purpose: Main/About Flask Blueprint

from flask import Blueprint, render_template, abort, send_file
from src.lib import getpageinfo, csvfile2list, md2html

main_bp = Blueprint('main_bp', __name__, template_folder='templates')

pagemeta = csvfile2list("config/pagemeta.csv")
for i in pagemeta:
    if i["page"] == "about":
        subpagemeta = csvfile2list(i["index"])
        break

for i in subpagemeta:
    if i["page"] == "root":
        sections = csvfile2list(i["content"])
    elif i["page"] == "privacy":
        pp_content = md2html(i["content"])

for i in sections:
    i["rendered"] = md2html(i["content"])
    
# Main About Page
@main_bp.route("/")
def index():
    return render_template("main_about.jinja2", pageinfo = getpageinfo("about", "root"), sections = sections)

# Privacy Policy
@main_bp.route("/privacy/")
def privacy():
    return render_template("main_privacy.jinja2", pageinfo = getpageinfo("about", "root"), content = pp_content)

@main_bp.route("/robots.txt")
def robots():
    return send_file("robots.txt")