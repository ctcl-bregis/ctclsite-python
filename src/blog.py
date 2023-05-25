# ctclsite-python - CTCL 2020-2023
# May 20, 2023 - May 25, 2023
# Purpose: Blog Flask Blueprint

from flask import Blueprint, render_template, abort, request
from src.lib import getpageinfo, csvfile2list, md2html

blog_bp = Blueprint('blog_bp', __name__, template_folder='templates')

pageindex = csvfile2list("config/pagemeta.csv")

for i in pageindex:
    if i["page"] == "blog":
        subpageindex = csvfile2list(i["index"])

# Projects List Page
@blog_bp.route("/")
def index():
    # Sort the posts descending by page name, which is numbered
    posts = sorted(subpageindex, key=lambda d: d['page'], reverse = True) 
    
    return render_template("blog_menu.jinja2", pageinfo = getpageinfo("blog", "root"), posts = posts)

# Projects Content Page
@blog_bp.route("/<page>/")
def projectpage(page):
    for i in subpageindex:
        if i["page"] == page:
            content = i["content"]
            break
    
    content = md2html(content)
    
    return render_template("blog_post.jinja2", pageinfo = getpageinfo("blog", page), content = content)
