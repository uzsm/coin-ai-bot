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