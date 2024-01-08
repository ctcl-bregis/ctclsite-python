# ctclsite-python - CTCL 2020-2024
# File: build.py
# Purpose: Creates various files used by the software
# Created: September 21, 2023
# Modified: January 7, 2024

import os, json, sys
from django.core.management.base import BaseCommand, CommandError
from django.core.management.utils import get_random_secret_key
from scss import Compiler
from scss.namespace import Namespace
from scss.types import String, Map
from csscompressor import compress

# Function that keeps error messages consistent
def perror(func, message):
    print(f"build.py {func} ERROR: {message}")
    sys.exit(1)

# Same function as perror but it does not exit
def pwarn(func, message):
    print(f"build.py {func} WARNING: {message}")

def compilescss(path, namespace):
    if not os.path.exists(path):
        perror("compilescss", "{path} does not exist")

    with open(path) as f:
        scss_src = f.read()

    try:
        css = Compiler(namespace = namespace).compile_string(scss_src)
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
            with open("config/config.json") as f:
                configjson = json.loads(f.read())["config"]
        except FileNotFoundError:
            perror("config loader", "config/config.json does not exist. Current working directory is \"{cwd}\".")
        except (json.JSONDecodeError, json.decoder.JSONDecodeError) as e:
            perror("config loader", "Exception \"{e}\" raised by JSON library")

        if not os.path.exists("build/"):
            os.mkdir("build/")

        main_css = {}
        lite_css = {}

        # configjson["styling_colors"] without "enabled"; {<theme>: {"color": <color>, "fgcolor": <color>}}
        themes = {}
        for key, value in configjson["styling_colors"].items():
            #themevalues = Map()

            themevalues = Map([(String("color"), String(value["color"])), (String("fgcolor"), String(value["fgcolor"]))])

            themes[String(key)] = themevalues

        for key, value in configjson["styling_colors"].items():
            if value["enabled"] == "true":
                namespace = Namespace()
                namespace.set_variable("$theme", String(value["color"], quotes=None))
                # "textcolor" is only for certain text elements that have a background of "theme"
                namespace.set_variable("$fgcolor", String(value["fgcolor"], quotes=None))

                # Dictionary of all themes put into a map for mainly styling blog post and project title boxes
                namespace.set_variable("$themes", Map(list(themes.items())))

                common_css = compilescss(configjson["main_scss"], namespace)
                main_css[key] = common_css

                common_css = compilescss(configjson["lite_scss"], namespace)
                lite_css[key] = common_css

        # Build "main" CSS
        if not os.path.exists("build/main/"):
            os.mkdir("build/main/")

        # Build "lite" CSS
        if not os.path.exists("build/lite/"):
            os.mkdir("build/lite/")

        with open(configjson["main_scss_comp"], "w") as f:
            f.write(json.dumps(main_css))

        with open(configjson["lite_scss_comp"], "w") as f:
            f.write(json.dumps(lite_css))