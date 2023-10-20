# ctclsite-python - CTCL 2020-2023
# File: middleware.py
# Purpose: Logging middleware for Django
# Created: August 30, 2023
# Modified: October 7, 2023

import os, csv, tarfile
from datetime import datetime

log_header = ["time", "ip", "port", "url", "refer", "useragent"]
log_latest = "logger/latest.csv"
log_dir = "logger/"
log_max_length = 10000

class LoggerMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        # One-time configuration and initialization.
         # Make the directory if it does not exist
        if not os.path.exists(log_dir):
            os.mkdir(log_dir)

    def __call__(self, request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.
        response = self.get_response(request)
        entry = {}

        now = datetime.now()
        timestr = now.strftime("%Y-%b-%d-%k-%M-%S").lower()
        if not os.path.exists(log_latest):
            with open(log_latest, "w", encoding='UTF8', newline='') as f:
                writer = csv.DictWriter(f, fieldnames = log_header)
                writer.writeheader()

        # TODO: Speed this up?
        count = 0
        with open(log_latest, "r") as f:
            for count, line in enumerate(f):
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

        entry["time"] = timestr
        entry["ip"] = request.META["REMOTE_ADDR"]
        entry["port"] = request.META["SERVER_PORT"]
        entry["url"] = request.path
        if "HTTP_REFERER" in request.META:
            entry["refer"] = request.META["HTTP_REFERER"]
        else:
            entry["refer"] = ""

        ua = request.META["HTTP_USER_AGENT"]
        # Keep log from being filled by extremely long user agents, usually from malicious users
        if len(ua) > 256:
            entry["useragent"] = "!! User Agent Too Long !!"
        else:
            entry["useragent"] = ua

        with open(log_latest, "a") as f:
            writer = csv.DictWriter(f, fieldnames = log_header)
            writer.writerow(entry)

        return response
