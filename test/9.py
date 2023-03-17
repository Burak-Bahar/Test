
if __name__ == "__main__":
    dictinary = {
        "AXO145" : "<url>https://xcd32112.smart_meter.com</url>"
    }

    a = dictinary["AXO145"].find("://")
    print(dictinary["AXO145"][a+3:-6])