# ctclsite-python - CTCL 2020-2023
# File: middleware.py
# Purpose: Logging middleware for Django
# Created: August 30, 2023
# Modified: December 22, 2023

import os, csv, tarfile
from datetime import datetime

# Guide:
# time: Timestamp of access
# ip: Client IP
# port: Server port accessed
# url: Webpage requested
# refer: Referred page
# useragent: Client user agent
# contentlength: Content-Length HTTP header
# contenttype: Content-Type HTTP header
# host: Server host accessed
# connection: Connection HTTP header
# cachecontrol: Cache-Control HTTP header
# secuabrowser: Sec-Ch-Ua HTTP header for browser version
# secuamobile: Sec-Ch-Ua-Mobile HTTP header for detecting a mobile browser
# secuaplatform: Sec-Ch-Ua-Platform HTTP header for detecting browser platform
# dnt: Is Do Not Track enabled
# httpsupgrade: Upgrade-Insecure-Requests HTTP header
# accept: Accepted formats
# secfetchsite: Sec-Fetch-Site HTTP header
# secfetchmode: Sec-Fetch-Mode HTTP header
# secfetchuser: Sec-Fetch-User HTTP header
# secfetchdest: Sec-Fetch-Dest HTTP header
# acceptencode: Accept-Encoding header
# acceptlangs: Accept-Language header

#log_header = ["time", "ip", "port", "url", "refer", "useragent"]
log_header = [
    "time",
    "ip",
    "port",
    "url",
    "refer",
    "useragent",
    "contentlength",
    "contenttype",
    "host",
    "connection",
    "cachecontrol",
    "secuabrowser",
    "secuamobile",
    "secuaplatform",
    "dnt",
    "httpsupgrade",
    "accept",
    "secfetchsite",
    "secfetchmode",
    "secfetchuser",
    "secfetchdest",
    "acceptencode",
    "acceptlangs"
]

log_latest = "logger/server_latest.csv"
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

        if request.path.startswith("/inlog/"):
            return response

        httpheaders = request.headers

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

        # Keep log from being filled by extremely long fields usually from malicious users
        for key, value in httpheaders.items():
            if len(value) > 512:
                httpheaders[key] = f"!! {key} too long !!"

        print(httpheaders)

        try:
            entry["refer"] = httpheaders["Referer"]
        except:
            entry["refer"] = ""

        try:
            entry["useragent"] = httpheaders["User-Agent"]
        except:
            entry["useragent"] = ""

        try:
            entry["contentlength"] = httpheaders["Content-Length"]
        except:
            entry["contentlength"] = ""

        try:
            entry["contenttype"] = httpheaders["Content-Type"]
        except:
            entry["contenttype"] = ""

        try:
            entry["host"] = httpheaders["Host"]
        except:
            entry["host"] = ""

        try: 
            entry["connection"] = httpheaders["Connection"]
        except:
            entry["connection"] = ""

        try:
            entry["cachecontrol"] = httpheaders["Cache-Control"]
        except:
            entry["cachecontrol"] = ""

        try:
            entry["secuabrowser"] = httpheaders["Sec-Ch-Ua"]
        except:
            entry["secuabrowser"] = ""

        try:
            entry["secuamobile"] = httpheaders["Sec-Ch-Ua-Mobile"]
        except:
            entry["secuamobile"] = ""

        try:
            entry["secuaplatform"] = httpheaders["Sec-Ch-Ua-Platform"]
        except:
            entry["secuaplatform"] = ""

        try:
            entry["dnt"] = httpheaders["Dnt"]
        except:
            entry["dnt"] = ""

        try:
            entry["httpsupgrade"] = httpheaders["Upgrade-Insecure-Requests"]
        except:
            entry["httpsupgrade"] = ""

        try:
            entry["accept"] = httpheaders["Accept"]
        except:
            entry["accept"] = ""

        try:
            entry["secfetchsite"] = httpheaders["Sec-Fetch-Site"]
        except:
            entry["secfetchsite"] = ""

        try:
            entry["secfetchmode"] = httpheaders["Sec-Fetch-Mode"]
        except:
            entry["secfetchmode"] = ""

        try:
            entry["secfetchuser"] = httpheaders["Sec-Fetch-User"]
        except:
            entry["secfetchuser"] = ""

        try:
            entry["secfetchdest"] = httpheaders["Sec-Fetch-Dest"]
        except:
            entry["secfetchdest"] = ""

        try:
            entry["acceptencode"] = httpheaders["Accept-Encoding"]
        except:
            entry["acceptencode"] = ""

        try:
            entry["acceptencode"] = httpheaders["Accept-Encoding"]
        except:
            entry["acceptencode"] = ""

        try:
            entry["acceptlangs"] = httpheaders["Accept-Language"]
        except:
            entry["acceptlangs"] = ""

        with open(log_latest, "a") as f:
            writer = csv.DictWriter(f, fieldnames = log_header)
            writer.writerow(entry)


        return response
