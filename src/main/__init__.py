# ctclsite-python - CTCL 2023
# May 15, 2023 - May 17, 2023
# Purpose: Main/About Flask Blueprint

from flask import Blueprint, render_template, abort
from src.lib import getpageinfo, csvfile2list
import csv
import markdown2 as markdown

main_bp = Blueprint('main_bp', __name__, template_folder='templates')

@main_bp.route("/")
def index():
    
    
    
    return render_template("main_about.jinja2")

@main_bp.route("/privacy/")
def privacy():
    with open("config/about/about_privacy.md") as f:
        content = markdown.markdown(f.read())
    
    return render_template("main_privacy.jinja2", content = content)
    
    
