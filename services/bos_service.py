def detect_bos(structure, candles):
    """
    Break Of Structure (BOS)

    Qaytaradi:
    [
        {
            "type": "BULLISH",
            "level": 118523.5,
            "pivot_index": 55,
            "break_index": 72,
            "price": 118523.5
        }
    ]
    """

    bos = []

    if len(structure) < 2:
        return bos

    for point in structure:

        label = point["label"]

        # Faqat HH va LL larni tekshiramiz
        if label not in ("HH", "LL"):
            continue

        level = point["price"]
        pivot_index = point["index"]

        # Pivotdan keyingi shamlarni tekshirish
        for i in range(pivot_index + 1, len(candles)):

            candle = candles[i]

            # Bullish BOS
            if label == "HH":

                if candle["close"] > level:

                    bos.append({

                        "type": "BULLISH",

                        "level": level,

                        "price": level,

                        "pivot_index": pivot_index,

                        "break_index": i

                    })

                    break

            # Bearish BOS
            else:

                if candle["close"] < level:

                    bos.append({

                        "type": "BEARISH",

                        "level": level,

                        "price": level,

                        "pivot_index": pivot_index,

                        "break_index": i

                    })

                    break

    return bos