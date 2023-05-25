# ctclsite-python - CTCL 2020-2023
# May 15, 2023 - May 25, 2023
# Purpose: App initialization

from flask import Flask, request, Response
from datetime import datetime
import os, csv, tarfile
from css_html_js_minify import process_single_css_file

log_header = ["time", "ip", "url", "referrer", "useragent"]
log_latest = "log/latest.csv"
log_dir = "log/"
log_max_length = 10000

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
    if not os.path.exists("config/styling.min.css"):
        process_single_css_file("config/styling.css", overwrite=False)
    
    # Make the log directory if it does not exist
    if not os.path.exists("log/"):
        os.makedirs("log/")
    
    @app.before_request
    def log():
        now = datetime.now()
        timestr = now.strftime("%b-%m-%Y-%k-%M-%S").lower()
        if not os.path.exists(log_latest):
            with open(log_latest, "w", encoding='UTF8', newline='') as f:
                writer = csv.writer(f)
                writer.writerow(log_header)
        
        # TODO: Speed this up?
        count = 0
        with open(log_latest, "r") as fp:
            for count, line in enumerate(fp):
                pass
        
        if count > log_max_length:
            arc_name = f"{log_dir}log_{timestr}"
        
            # rename current log file before adding it to the archive
            os.rename(log_latest, f"{arc_name}.csv")
        
            # create tar file with gzip compression
            tar = tarfile.open(f"{arc_name}.tar.gz", "w:gz", compresslevel=9)
            tar.add(f"{arc_name}.csv")
            tar.close()
        
            # Remove the old log file
            os.remove(f"{arc_name}.csv")
        
            # create another current log file
            with open(log_latest, "w", encoding='UTF8', newline='') as f:
                writer = csv.writer(f)
                writer.writerow(log_header)

        row = {}

        row["time"] = timestr
        try:
            row["ip"] = str(request.environ['HTTP_X_FORWARDED_FOR'])
        except:
            row["ip"] = "None"
            
        row["url"] = str(request.url)
        row["referrer"] = str(request.headers.get("Referer"))
        
        ua = str(request.headers.get('User-Agent'))
        # Keep log from being filled by extremely long user agents, usually from malicious users 
        if len(ua) > 256:
            row["useragent"] = "!! User Agent Too Long !!"
        else:
            row["useragent"] = ua
    
        with open(log_latest, "a") as f:
            writer = csv.DictWriter(f, fieldnames = log_header)
            writer.writerow(row)
    
    
    return app
