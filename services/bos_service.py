def detect_bos(structure, candles):

    bos = []

    if len(structure) < 2:
        return bos

    for point in structure:

        label = point["label"]

        # Faqat HH yoki LL
        if label not in ("HH", "LL"):
            continue

        level = point["price"]

        for candle in candles[point["index"] + 1:]:

            # Bullish BOS
            if label == "HH":

                if candle["close"] > level:

                    bos.append({

                        "type": "BULLISH",

                        "index": point["index"],

                        "price": level,

                        
                    })

                    break

            # Bearish BOS
            else:

                if candle["close"] < level:

                    bos.append({

                        "type": "BEARISH",

                        "index": point["index"],

                        "price": level,

                       

                    })

                    break

    return bos