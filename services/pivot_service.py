def detect_pivots(candles, left=2, right=2):

    pivots = []

    total = len(candles)

    for i in range(left, total - right):

        current = candles[i]

        high = current["high"]
        low = current["low"]

        is_high = True
        is_low = True

        # Chap tomonni tekshirish
        for j in range(i - left, i):

            if candles[j]["high"] >= high:
                is_high = False

            if candles[j]["low"] <= low:
                is_low = False

        # O'ng tomonni tekshirish
        for j in range(i + 1, i + right + 1):

            if candles[j]["high"] >= high:
                is_high = False

            if candles[j]["low"] <= low:
                is_low = False

        # Natijani saqlash
        if is_high:
            pivots.append({
               
                "index": i,
                "type": "HIGH",
                "price": high,
                "strength": 0,
                "confirmed": False

            })

        if is_low:
            pivots.append({
                "index": i,
                "type": "LOW",
                "price": low,
                "strength": 0,
                "confirmed": False

            })

    return pivots