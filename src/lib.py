# ctclsite-python - CTCL 2023
# May 15, 2023 - May 16, 2023
# Purpose: Commonly used functions

import csv

def csvfile2list(path):
    with open(path) as f:
        content = list(csv.DictReader(f))
        
    return content

def getpageinfo(subindex, page):
    
    pageinfo = {}
    
    pagemeta = csvfile2list("config/pagemeta.csv")
    
    for i in pagemeta:
        if subindex == i["page"]:
            subindex_path = i["index"]
            break
    else:
        raise Exception(f"{subindex} does not exist in config/pagemeta.csv")
    
    subpagemeta = csvfile2list(subindex_path)
        
    for i in subpagemeta:
        if page == i["page"]:
            pageinfo["desc"] = i["desc"]
            pageinfo["title"] = i["title"]
            pageinfo["color"] = i["color"]
            pageinfo["content"] = i["content"]
            break
    else:
        raise Exception(f"{page} does not exist in {subindex_path}")
    
    with open("config/styling.css") as f:
        # TODO: Add CSS Minimizer
        styling = f.read()
        pageinfo["css"] = styling.replace("{{ color }}", pageinfo["color"])
        
    pageinfo["subindex"] = subindex
    
    return pageinfo
