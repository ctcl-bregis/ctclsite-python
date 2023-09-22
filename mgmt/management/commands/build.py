# ctclsite-python - CTCL 2020-2023
# File: build.py
# Purpose: Creates various files used by the software
# Created: September 21, 2023
# Modified: September 21, 2023

import os, json, sys
from django.core.management.base import BaseCommand, CommandError
from scss import Compiler

# Function that keeps error messages consistent
def perror(func, message):
    print(f"build.py {func} ERROR: {message}")
    sys.exit(1)

# Same function as perror but it does not exit
def pwarn(func, message):
    print(f"build.py {func} WARNING: {message}")

def compilescss(path):
    if not os.path.exists(path):
        perror("compilescss", "{path} does not exist")

    with open(path) as f:
        scss_src = f.read()

    try:
        theme["css"] = Compiler().compile_string(theme["scss"])
    except Exception as err:
        pwarn("configthemes", f"Sass compilation error while processing {path}: {err}")


class Command(BaseCommand):
    help = "Generates all of the needed files for the application."
    cwd = os.getcwd()

    def handle(self, *args, **options):
        # Get global config
        try:
            with open("mgmt/config.json") as f:
                configjson = json.loads(f.read())["config"]
        except FileNotFoundError:
            perror("config loader", "config/config.json does not exist. Current working directory is \"{cwd}\".")
        except (json.JSONDecodeError, json.decoder.JSONDecodeError) as e:
            perror("config loader", "Exception \"{e}\" raised by JSON library")

        common_css = compilescss(configjson["scss"])
        with open(configjson["scss_comp"], "w") as f:
            f.write(common_css)

