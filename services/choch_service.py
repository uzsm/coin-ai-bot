def detect_choch(structure):

    choch = []

    if len(structure) < 4:
        return choch

    for i in range(3, len(structure)):

        s1 = structure[i - 3]
        s2 = structure[i - 2]
        s3 = structure[i - 1]
        s4 = structure[i]

        # Bullish -> Bearish
        if (
            s1["label"] == "HH"
            and s2["label"] == "HL"
            and s3["label"] == "LH"
            and s4["label"] == "LL"
        ):

            choch.append({
                "type": "BEARISH_CHOCH",
                "index": s4["index"],
                "price": s4["price"]
            })

        # Bearish -> Bullish
        if (
            s1["label"] == "LL"
            and s2["label"] == "LH"
            and s3["label"] == "HL"
            and s4["label"] == "HH"
        ):

            choch.append({
                "type": "BULLISH_CHOCH",
                "index": s4["index"],
                "price": s4["price"]
            })

    return choch