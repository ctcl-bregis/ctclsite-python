# 5.5.4 - February 26, 2024
Development of the second ctclsite-rust rewrite has started. Another small feature has been added for the time being.

## Additons

- HTML image titles; mouseover text on Blog icons

# 5.5.3 - February 23, 2024
This update brings some minor fixes and functionality relating to styling and links.

## Additions

- Added "bookmark" functionality to automatically scroll to a specific section. For example: ctcl-tech.com/#contact would scroll to the Contact section.

## Fixes

- Use of "id" attributes for styling
- Right border of section buttons when automatically set to full width by common.js

# 5.5.2 - February 4, 2024
Content updates along with this update include: Addition of description to pages that did not have one, blog post, theme color changes, project details and link fixes.

## Fixes

- Overall fixes to templates
- Improvements to the link page for the college club
- Improvments to SCSS

# 5.5.1 - January 31, 2024

## Fixes

- HTML descriptions are no longer present if the description is empty

# 5.5.0 - January 31, 2024

## Additions

- "bcc_cc" app relating to pages for use by a college club
- Link to home page in the footer

## Fixes

- Theme color for embeds should now be defined

# 5.4.3 - January 28, 2024

## Fixed
- Link fixes in templates

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
