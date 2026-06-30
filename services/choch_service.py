def detect_choch(structure):

    choch = []

    if len(structure) < 4:
        return choch

    current_trend = None

    for i in range(3, len(structure)):

        s1 = structure[i - 3]
        s2 = structure[i - 2]
        s3 = structure[i - 1]
        s4 = structure[i]

        # Trendni aniqlash
        if s1["label"] == "HH" and s2["label"] == "HL":
            current_trend = "BULLISH"

        elif s1["label"] == "LL" and s2["label"] == "LH":
            current_trend = "BEARISH"

        # Bullish -> Bearish ChoCH
        if current_trend == "BULLISH":

            if (
                s3["label"] == "LH"
                and s4["label"] == "LL"
            ):

                choch.append({

                    "type": "BEARISH_CHOCH",

                    "index": s4["index"],

                    "price": s4["price"],

                    "broken_level": s2["price"]

                })

                current_trend = "BEARISH"

        # Bearish -> Bullish ChoCH
        elif current_trend == "BEARISH":

            if (
                s3["label"] == "HL"
                and s4["label"] == "HH"
            ):

                choch.append({

                    "type": "BULLISH_CHOCH",

                    "index": s4["index"],

                    "price": s4["price"],

                    "broken_level": s2["price"]

                })

                current_trend = "BULLISH"

    return choch