def detect_bos(structure, candles):

    bos_list = []

    for point in structure:

        if point["type"] == "HIGH":

            level = point["price"]

            for candle in candles[point["index"] + 1:]:

                if candle["close"] > level:

                    bos_list.append({
                        "type": "BULLISH",
                        "level": level
                    })

                    break

        else:

            level = point["price"]

            for candle in candles[point["index"] + 1:]:

                if candle["close"] < level:

                    bos_list.append({
                        "type": "BEARISH",
                        "level": level
                    })

                    break

    return bos_list