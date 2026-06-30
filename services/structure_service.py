def build_structure(swings):

    structure = []

    last_high = None
    last_low = None

    for swing in swings:

        label = ""

        if swing["type"] == "HIGH":

            if last_high is None:
                label = "H"

            elif swing["price"] > last_high:
                label = "HH"

            else:
                label = "LH"

            last_high = swing["price"]

        else:

            if last_low is None:
                label = "L"

            elif swing["price"] > last_low:
                label = "HL"

            else:
                label = "LL"

            last_low = swing["price"]

        structure.append({

            "index": swing["index"],

            "type": swing["type"],

            "price": swing["price"],

            "label": label

        })

    return structure

def analyze_structure(structure):

    result = {
        "trend": None,
        "last_high": None,
        "last_low": None,
        "last_hh": None,
        "last_hl": None,
        "last_lh": None,
        "last_ll": None,

        "current": None,
        "previous": None,

        "structure": structure
    }

    for item in structure:

        if item["type"] == "HIGH":
            result["last_high"] = item

        if item["type"] == "LOW":
            result["last_low"] = item

        if item["label"] == "HH":
            result["last_hh"] = item

        elif item["label"] == "HL":
            result["last_hl"] = item

        elif item["label"] == "LH":
            result["last_lh"] = item

        elif item["label"] == "LL":
            result["last_ll"] = item
            
    # Trend aniqlash

    
    if len(structure) >= 2:
     result["previous"] = structure[-2]
     result["current"] = structure[-1] 
     
    if result["current"]:

     label = result["current"]["label"]

    if label in ("HH", "HL"):
        result["trend"] = "BULLISH"

    elif label in ("LH", "LL"):
        result["trend"] = "BEARISH"

    else:
        result["trend"] = "SIDEWAYS"

    return result