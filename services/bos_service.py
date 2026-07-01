def detect_bos(structure, candles):
    """
    Break Of Structure (BOS)

    Return:

    [
        {
            "type": "BULLISH",
            "level": 118523.5,
            "price": 118523.5,
            "pivot_index": 55,
            "break_index": 72,
            "index": 72
        }
    ]
    """

    bos = []

    if len(structure) < 2:
        return bos

    for point in structure:

        label = point["label"]

        # Faqat HH va LL lar
        if label not in ("HH", "LL"):
            continue

        level = point["price"]
        pivot_index = point["index"]

        # Pivotdan keyingi shamlarni tekshiramiz
        for i in range(pivot_index + 1, len(candles)):

            candle = candles[i]

            # ==========================
            # Bullish BOS
            # ==========================

            if label == "HH":

                if candle["close"] > level:

                    bos.append({

                        "type": "BULLISH",

                        "level": level,

                        "price": level,

                        "pivot_index": pivot_index,

                        "break_index": i,

                        "index": i

                    })

                    break

            # ==========================
            # Bearish BOS
            # ==========================

            elif label == "LL":

                if candle["close"] < level:

                    bos.append({

                        "type": "BEARISH",

                        "level": level,

                        "price": level,

                        "pivot_index": pivot_index,

                        "break_index": i,

                        "index": i

                    })

                    break

    return bos