def detect_trend(structure):

    hh = 0
    hl = 0
    lh = 0
    ll = 0

    for item in structure:

        if item["label"] == "HH":
            hh += 1

        elif item["label"] == "HL":
            hl += 1

        elif item["label"] == "LH":
            lh += 1

        elif item["label"] == "LL":
            ll += 1

    bullish = hh + hl
    bearish = lh + ll

    if bullish > bearish:
        return "BULLISH"

    elif bearish > bullish:
        return "BEARISH"

    return "SIDEWAYS"