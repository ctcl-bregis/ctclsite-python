# 5.1.0 - December 22, 2023
Yet another total rewrite of the website, finally adding client-side scripts for mainly cosmetic features.

## Additions

- Significant improvement to the front-end part of the website, adding content using JavaScript
- Compatability version of the website that does not use JavaScript and advanced CSS features
- Current website Django "app" renamed to lite and is now the more accessible version of the website
- Content is now defined under the "config" directory
- Significant upgrade to the logger
- Tested on Django 5.0

## Fixes

- Fixed Debug mode being enabled in production
- Link color on some browsers, first observed with Steam's implementation of Chromium

## Changes

- Minor changes to the pix5x5 font used throughout the website
- The "Play" font is now used for body instead of Arial

## Removals

- RAMList was removed indefinitely, except for its configuration files

# 4.1.1 - October 26, 2023

## Fixes

- Fixed "File operation error when opening" on Privacy Policy and Licensing pages. That could have lead to a potential DoS if the page was reloaded too many times.

# 4.1.0 - October 20, 2023

## What's different from 3.2.4

- Total rewrite of the CTCL website now using the Django web framework
- All CSV-based configuration files were replaced by JSON
- Images are now in the WEBP format instead of PNG to save bandwidth usage
- SCSS support added for styling
- The RAMList page is disabled for this release
