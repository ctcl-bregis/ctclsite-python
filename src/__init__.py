# ctclsite-python - CTCL 2023
# May 15, 2023 - May 20, 2023
# Purpose: App initialization

from flask import Flask
import os, csv
from css_html_js_minify import process_single_css_file

def mkapp():
    app = Flask(__name__, instance_relative_config = False)
    app.url_map.strict_slashes = True
    
    from src.main import main_bp
    from src.ramlist import rl_bp
    from src.projects import projects_bp
    from src.blog import blog_bp
    
    app.register_blueprint(main_bp)
    app.register_blueprint(rl_bp, url_prefix = "/ramlist")
    app.register_blueprint(projects_bp, url_prefix = "/projects")
    app.register_blueprint(blog_bp, url_prefix = "/blog")
    
    # Minimize CSS
    process_single_css_file("config/styling.css", overwrite=False)
    
    return app
