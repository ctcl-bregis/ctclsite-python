# ctclsite-python - CTCL 2020-2023
# File: middleware.py
# Purpose: Logging middleware for Django
# Created: August 30, 2023
# Modified: September 2, 2023

import os, csv

class LoggerMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        # One-time configuration and initialization.

        # Make the directory if it does not exist
        if not os.path.exists("logger/logs/"):
            os.mkdir("logger/logs/")

    def __call__(self, request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.

        response = self.get_response(request)

        with open("logger/logs/latest.csv", "a") as f:
            writer = csv.writer(f)
            writer.writerow(entry)


        return response