# ctclsite-python - CTCL 2020-2023
# File: build.py
# Purpose: Creates various files used by the software
# Created: September 21, 2023
# Modified: November 23, 2023

import os, json, sys
from django.core.management.base import BaseCommand, CommandError
from django.core.management.utils import get_random_secret_key
from scss import Compiler
from csscompressor import compress

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
        css = Compiler().compile_string(scss_src)
    except Exception as err:
        perror("configthemes", f"Sass compilation error while processing {path}: {err}")

    try:
        css_comp = compress(css)
        return css_comp
    except Exception as err:
        perror("configthemes", f"CSS minimization error while processing {path}: {err}")

class Command(BaseCommand):
    help = "Generates all of the needed files for the application."
    cwd = os.getcwd()

    def handle(self, *args, **options):
        # CS_DEBUG should be something other than "False" when running in production, the key should be generated then
        if os.environ["CS_DEBUG"] != "False":
            django_key = get_random_secret_key()
            
            with open("key.txt", "w") as f:
                f.write(django_key)

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

