// ctclsite-python - CTCL 2020-2024
// File: common.js
// Purpose: Commonly loaded JavaScript script for various functions, see comments below
// Created: January 8, 2024
// Modified: January 8, 2024

// Extend the header to fit the entire section width if it is past a certain width
var sectionHeaders = document.getElementsByClassName("sectionheader");
for (let i = 0; i < sectionHeaders.length; i++) {
    var sectionHeader = sectionHeaders[i];
    var parentSectionWidth = sectionHeader.parentElement.getBoundingClientRect().width;

    console.log(sectionHeader.getBoundingClientRect().width / parentSectionWidth);
    if ((sectionHeader.getBoundingClientRect().width / parentSectionWidth) > 0.75) {
        console.log("section modified")
        sectionHeader.setAttribute("style", "width: 100%");
    }
}

