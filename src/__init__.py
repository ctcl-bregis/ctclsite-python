# ctclsite-python - CTCL 2023
# May 15, 2023 - May 17, 2023
# Purpose: App initialization

from flask import Flask
import os

def mkapp():
    app = Flask(__name__, instance_relative_config = False)
    app.url_map.strict_slashes = True
    
    from src.ramlist import rl_bp
    from src.main import main_bp
    
    app.register_blueprint(main_bp, url_prefix = "/")
    app.register_blueprint(rl_bp, url_prefix = "/ramlist")
    
    return app
