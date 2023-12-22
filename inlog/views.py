# ctclsite-python - CTCL 2020-2023
# File: inlog/views.py
# Purpose: Views for the client-side logging feature
# Created: December 16, 2023
# Modified: December 20, 2023

from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, HttpResponseNotAllowed, HttpResponseBadRequest
import json, os, csv, hashlib
from app import lib
from datetime import datetime

# Headers to have associated data go under
log_header = ["time", "timeZone", "localIp", "extIp", "webGlDebug", "webGlVendor", "webGlRenderer", "cpuCores", "memSize", "maxTp", "plat", "screenX", "screenY", "screenPixRatio", "screenPixDepth", "canvasFp", "onLine", "pdfViewer", "dntEnabled", "langs", "prod", "prodSub", "userAgent", "vend", "innerHeight", "innerWidth"]
# The "latest" log to write to
log_latest = "logger/client_latest.csv"
# The directory that logs go under
log_dir = "logger/"
# Maximum log entries per file
log_max_length = 10000

@csrf_exempt
def incoming(request):
    # Why is this the first time I ever had to do this?
    global log_header

    if request.method == "POST":
        data = json.loads(request.body)
    else:
        # Return "Not Allowed" if the client tries to use GET on this URL
        return HttpResponseNotAllowed("")

    # Check if the data sent has keys that match the log_header list, this is to prevent Internal Server Errors from bogus data
    # Once again omit "time"
    if list(data.keys()) != log_header[1:]:
        return HttpResponseBadRequest("")

    validated_data = {}
    # Convert everything to a string and replace any strings that are too long
    for key, value in data.items():
        if len(str(value)) < 256:
            validated_data[key] = str(value)
        else:
            validated_data[key] = f"!! {key} too long !!"

    # This is probably very inefficient
    if not os.path.exists(log_latest):
        with open(log_latest, "w", encoding='UTF8', newline='') as f:
                writer = csv.DictWriter(f, fieldnames = log_header)
                writer.writeheader()

    # Timestamp is separate from the sent data
    now = datetime.now()
    timestr = now.strftime("%Y-%b-%d-%k-%M-%S").lower()
    validated_data["time"] = timestr

    # TODO: Speed this up?
    count = 0
    with open(log_latest, "r") as f:
        for count, line in enumerate(f):
            pass

    # If the log is currently too long, back it up
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

    with open(log_latest, "a") as f:
        writer = csv.DictWriter(f, fieldnames = log_header)
        writer.writerow(validated_data)

    return HttpResponse("")

# URL that just returns the IP address of the request
def getip(request):
    xforwardedfor = request.META.get('HTTP_X_FORWARDED_FOR')

    if xforwardedfor:
        ip = xforwardedfor.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')

    return HttpResponse(ip)