ctclsite-python "Apache Trout"

This is the website backend used for the website at ctcl-tech.com, formerly crazyblockstech.com

Due to incompatible code in the dependencies that this app uses, an environment of Python 3.10 must be used.

## Directory structure
The "app" directory acts as global configuration data and contains the templates and static files.

The "config" directory contains all of the definitions of the content used in the website

The "lite" directory is the views for the version of the website that does not have client-side scripts and is meant for a wider range of devices and browsers

The "main" directory is the views for the version of the website that makes use of client-side scripts and is viewed by default

The "mgmt" directory contains custom management commands and some files to be processed when the "build" management command is used.
