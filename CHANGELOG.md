# 5.4.2 - January 14, 2024
Authored on: "Polybutylene Terephthalate", "Polymethylmethacrylate"

## Changes
- Removed unnecessary directories 

## Fixed
- Major fixes to clientinfo.js
- Major fixes to common.js
- Fixed text size for blog post titles

# 5.4.1 - January 11, 2024
Authored on: "Polymethylmethacrylate"

## Removed
- Unused version definition
- Django version specification in requirements

# 5.4.0 - January 9, 2024
Authored on: "Polybutylene Terephthalate", taken over on "Polymethylmethacrylate"

## Additions
- common.js script, currently its only purpose is to automatically resize section headers

## Changes
- Various SCSS/CSS and HTML fixes and improvements
- As of the last update, Pix5x5 was split into its own project; repository
- Template consolidation
- Theme consistency
- Improvements to the "lite" version
- runner_dev now always runs the build command

## Fixed
- clientinfo.js loading when it shouldn't

# 5.3.0 - January 7, 2024
Authored on: "Polybutylene Terephthalate", "Tetrahydrocannabinol" for creating just one directory

## Additions

- "Services" page for offered services
- Image icons for blog post entries

## Changes

- Template consolidation
- Interface text no longer uses header types for sizing
- Privacy Policy page no longer loads clientinfo.js
- Animated buttons for project and blog post items
- Various CSS and HTML fixes

# 5.2.0 - December 31, 2023
Authored on: "Polybutylene Terephthalate"

## Additions

- Descriptions for project categories

## Changes

- Look of the About sections

# 5.1.0 - December 22, 2023
Authored on: "Polybutylene Terephthalate"

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

- RAMList removed indefinitely, except for its configuration files

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
